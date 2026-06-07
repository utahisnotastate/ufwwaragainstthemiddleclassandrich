#include <M5Unified.h>
#include <ArduinoJson.h>
#include <Wire.h>

namespace {

constexpr uint8_t PBHUB_ADDR = 0x61;
volatile bool running_ = false;
TaskHandle_t poll_task_ = nullptr;

int fsr_channels_[4] = {0, 1, 2, 3};
int strike_threshold_ = 1800;
int memory_slots_ = 64;
uint32_t write_count_ = 0;
uint32_t last_strike_[4] = {0, 0, 0, 0};

int readPbHubChannel(int channel) {
    Wire.beginTransmission(PBHUB_ADDR);
    Wire.write(static_cast<uint8_t>(channel));
    if (Wire.endTransmission(false) != 0) {
        return -1;
    }
    if (Wire.requestFrom(PBHUB_ADDR, static_cast<uint8_t>(2)) != 2) {
        return -1;
    }
    return Wire.read() | (Wire.read() << 8);
}

void pollLoop(void*) {
    while (running_) {
        for (int i = 0; i < 4; ++i) {
            int value = readPbHubChannel(fsr_channels_[i]);
            if (value < 0) {
                continue;
            }
            uint32_t now = millis();
            if (value < strike_threshold_ && (now - last_strike_[i]) > 300) {
                last_strike_[i] = now;
                write_count_ = (write_count_ + 1) % memory_slots_;
                Serial.printf("[DDR] Memory write CH%d val=%d slot=%lu\n", fsr_channels_[i], value,
                              static_cast<unsigned long>(write_count_));
            }
        }

        auto* gfx = M5.Display.get();
        if (gfx) {
            gfx->fillRect(0, 0, gfx->width(), 24, TFT_BLACK);
            gfx->setCursor(4, 4);
            gfx->setTextColor(TFT_CYAN);
            gfx->printf("AKASHIC DDR writes: %lu", static_cast<unsigned long>(write_count_));
        }
        vTaskDelay(pdMS_TO_TICKS(20));
    }
    vTaskDelete(nullptr);
}

}  // namespace

namespace artifacts {

bool mnemonic_ddr_start(const JsonDocument& manifest) {
    JsonVariantConst params = manifest["parameters"];
    if (!params.isNull()) {
        strike_threshold_ = params["strike_threshold"] | 1800;
        memory_slots_ = params["memory_slots"] | 64;
        JsonArrayConst channels = params["fsr_channels"];
        if (!channels.isNull()) {
            int idx = 0;
            for (JsonVariantConst ch : channels) {
                if (idx < 4) {
                    fsr_channels_[idx++] = ch.as<int>();
                }
            }
        }
    }

    Wire.begin(M5.Ex_I2C.getSDA(), M5.Ex_I2C.getSCL(), 400000UL);
    running_ = true;
    xTaskCreatePinnedToCore(pollLoop, "fsr_poll", 4096, nullptr, 2, &poll_task_, 1);
    Serial.println("[DDR] Mnemonic DDR Infinity — PbHub polling active");
    return true;
}

void mnemonic_ddr_stop() {
    running_ = false;
    vTaskDelay(pdMS_TO_TICKS(50));
    poll_task_ = nullptr;
}

}  // namespace artifacts
