#include <M5Unified.h>
#include <ArduinoJson.h>
#include <WiFi.h>
#include <esp_now.h>
#include <Wire.h>

namespace {

constexpr uint8_t TOF_ADDR = 0x29;
volatile bool running_ = false;
bool ops_halted_ = false;
int wave_threshold_mm_ = 180;
uint8_t worker_count_ = 6;

typedef struct {
    uint8_t node_id;
    uint8_t status;  // 0=halt, 1=run, 2=alert
    uint8_t color_id;
} WorkerPacket;

void onEspNowSent(const uint8_t* mac, esp_now_send_status_t status) {
    (void)mac;
    if (status != ESP_NOW_SEND_SUCCESS) {
        Serial.println("[WAR] ESP-NOW send failed");
    }
}

void broadcastWorkers(uint8_t command) {
    WorkerPacket pkt = {};
    pkt.status = command;
    uint8_t broadcast[6] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF};
    for (uint8_t i = 0; i < worker_count_; ++i) {
        pkt.node_id = i;
        pkt.color_id = i;
        esp_now_send(broadcast, reinterpret_cast<uint8_t*>(&pkt), sizeof(pkt));
    }
}

int readToFDistanceMm() {
    Wire.beginTransmission(TOF_ADDR);
    Wire.write(0x00);
    if (Wire.endTransmission(false) != 0) {
        return -1;
    }
    if (Wire.requestFrom(TOF_ADDR, static_cast<uint8_t>(2)) != 2) {
        return -1;
    }
    uint16_t raw = Wire.read() | (Wire.read() << 8);
    return static_cast<int>(raw);
}

void warRoomLoop(void*) {
    while (running_) {
        int dist = readToFDistanceMm();
        if (dist > 0 && dist < wave_threshold_mm_) {
            ops_halted_ = !ops_halted_;
            broadcastWorkers(ops_halted_ ? 0 : 1);
            Serial.printf("[WAR] ToF gesture — ops %s\n", ops_halted_ ? "HALTED" : "EXECUTE");
            vTaskDelay(pdMS_TO_TICKS(800));
        }

        auto* gfx = M5.Display.get();
        if (gfx) {
            gfx->fillScreen(TFT_BLACK);
            gfx->setCursor(4, 4);
            gfx->setTextColor(ops_halted_ ? TFT_RED : TFT_GREEN);
            gfx->printf("WAR ROOM %s", ops_halted_ ? "HALT" : "ACTIVE");
            gfx->setCursor(4, 20);
            gfx->setTextColor(TFT_WHITE);
            gfx->printf("Workers: %d  ToF:%dmm", worker_count_, dist);
        }
        vTaskDelay(pdMS_TO_TICKS(200));
    }
    vTaskDelete(nullptr);
}

}  // namespace

namespace artifacts {

bool war_room_start(const JsonDocument& manifest) {
    JsonVariantConst params = manifest["parameters"];
    if (!params.isNull()) {
        worker_count_ = params["worker_count"] | 6;
        wave_threshold_mm_ = params["wave_threshold_mm"] | 180;
    }

    WiFi.mode(WIFI_STA);
    if (esp_now_init() != ESP_OK) {
        Serial.println("[WAR] ESP-NOW init failed");
        return false;
    }
    esp_now_register_send_cb(onEspNowSent);

    Wire.begin(M5.Ex_I2C.getSDA(), M5.Ex_I2C.getSCL(), 400000UL);
    running_ = true;
    broadcastWorkers(1);
    xTaskCreatePinnedToCore(warRoomLoop, "war_room", 4096, nullptr, 2, nullptr, 1);
    Serial.println("[WAR] Tactical Command Table — ESP-NOW overlord online");
    return true;
}

void war_room_stop() {
    running_ = false;
    broadcastWorkers(0);
    esp_now_deinit();
    vTaskDelay(pdMS_TO_TICKS(50));
}

}  // namespace artifacts
