#include <M5Unified.h>
#include <ArduinoJson.h>
#include <cstring>

namespace {

volatile bool running_ = false;
TaskHandle_t osc_task_ = nullptr;
int mosfet_gpio_ = 1;
float frequency_hz_ = 7.83f;
int duty_percent_ = 50;
bool use_gamma_ = false;

void oscillatorLoop(void*) {
    const int period_us = static_cast<int>(1000000.0f / frequency_hz_);
    const int high_us = period_us * duty_percent_ / 100;
    const int low_us = period_us - high_us;

    pinMode(mosfet_gpio_, OUTPUT);

    while (running_) {
        digitalWrite(mosfet_gpio_, HIGH);
        delayMicroseconds(high_us);
        digitalWrite(mosfet_gpio_, LOW);
        delayMicroseconds(low_us);

        if (M5.BtnA.wasPressed()) {
            use_gamma_ = !use_gamma_;
            frequency_hz_ = use_gamma_ ? 40.0f : 7.83f;
            Serial.printf("[PAA] Mode switch: %.2f Hz\n", frequency_hz_);
        }
    }
    digitalWrite(mosfet_gpio_, LOW);
    vTaskDelete(nullptr);
}

void statusLoop(void*) {
    while (running_) {
        uint32_t color = use_gamma_ ? 0x4040ff : 0x00ff80;
        M5.displays(0).fillScreen(TFT_BLACK);
        if (auto* gfx = M5.Display.get()) {
            gfx->setTextColor(TFT_WHITE);
            gfx->setCursor(2, 2);
            gfx->printf("PAA %.2fHz", frequency_hz_);
            gfx->drawCircle(gfx->width() / 2, gfx->height() / 2, 10, color);
        }
        M5.update();
        vTaskDelay(pdMS_TO_TICKS(200));
    }
    vTaskDelete(nullptr);
}

}  // namespace

namespace artifacts {

bool psychotronic_start(const JsonDocument& manifest) {
    JsonVariantConst params = manifest["parameters"];
    if (!params.isNull()) {
        mosfet_gpio_ = params["mosfet_gpio"] | 1;
        duty_percent_ = params["duty_percent"] | 50;
        const char* mode = params["mode"] | "schumann";
        JsonVariantConst freqs = params["frequencies_hz"];
        if (strcmp(mode, "gamma") == 0) {
            use_gamma_ = true;
            frequency_hz_ = freqs["gamma"] | 40.0f;
        } else {
            frequency_hz_ = freqs["schumann"] | 7.83f;
        }
    }

    running_ = true;
    xTaskCreatePinnedToCore(oscillatorLoop, "paa_osc", 3072, nullptr, 3, &osc_task_, 0);
    xTaskCreatePinnedToCore(statusLoop, "paa_status", 3072, nullptr, 1, nullptr, 0);
    Serial.printf("[PAA] Psychotronic Amplifier — %.2f Hz (BtnA toggles gamma)\n", frequency_hz_);
    return true;
}

void psychotronic_stop() {
    running_ = false;
    vTaskDelay(pdMS_TO_TICKS(50));
    osc_task_ = nullptr;
}

}  // namespace artifacts
