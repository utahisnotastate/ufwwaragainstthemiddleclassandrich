#include <M5Unified.h>
#include <ArduinoJson.h>
#include <Wire.h>
#include <math.h>

namespace {

constexpr uint8_t DAC_ADDR = 0x60;
volatile bool running_ = false;
TaskHandle_t emit_task_ = nullptr;
int relay_gpio_ = 2;
float carrier_hz_ = 61.8f;
uint32_t phase_step_ = 0;

void writeDac(uint16_t value) {
    Wire.beginTransmission(DAC_ADDR);
    Wire.write(static_cast<uint8_t>((value >> 4) & 0xFF));
    Wire.write(static_cast<uint8_t>((value & 0x0F) << 4));
    Wire.endTransmission();
}

void emitLoop(void*) {
    pinMode(relay_gpio_, OUTPUT);
    const float two_pi = 6.2831853f;
    uint32_t sample_us = static_cast<uint32_t>(1000000.0f / (carrier_hz_ * 64.0f));

    while (running_) {
        for (int i = 0; i < 64; ++i) {
            float theta = two_pi * static_cast<float>(phase_step_ + i) / 64.0f;
            float sine = sinf(theta);
            uint16_t dac_val = static_cast<uint16_t>((sine + 1.0f) * 2047.5f);
            writeDac(dac_val);
            digitalWrite(relay_gpio_, sine < 0.0f ? HIGH : LOW);
            delayMicroseconds(sample_us);
        }
        phase_step_ = (phase_step_ + 1) % 64;

        if ((phase_step_ % 16) == 0) {
            Serial.println("[CHRONO] Phase-conjugate wave active @ 61.8Hz");
        }
    }
    digitalWrite(relay_gpio_, LOW);
    vTaskDelete(nullptr);
}

}  // namespace

namespace artifacts {

bool chrono_heal_start(const JsonDocument& manifest) {
    JsonVariantConst params = manifest["parameters"];
    if (!params.isNull()) {
        carrier_hz_ = params["carrier_hz"] | 61.8f;
        relay_gpio_ = params["relay_gpio"] | 2;
    }

    Wire.begin(M5.Ex_I2C.getSDA(), M5.Ex_I2C.getSCL(), 400000UL);
    running_ = true;
    xTaskCreatePinnedToCore(emitLoop, "chrono_emit", 4096, nullptr, 2, &emit_task_, 1);
    Serial.println("[CHRONO] Cellular Regenesis Chamber — Priore scalar field engaged");
    return true;
}

void chrono_heal_stop() {
    running_ = false;
    vTaskDelay(pdMS_TO_TICKS(50));
    emit_task_ = nullptr;
}

}  // namespace artifacts
