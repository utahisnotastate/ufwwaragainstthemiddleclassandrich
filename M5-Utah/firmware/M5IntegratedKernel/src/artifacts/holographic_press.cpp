#include <M5Unified.h>
#include <ArduinoJson.h>
#include <Wire.h>

namespace {

constexpr uint8_t GESTURE_ADDR = 0x73;
volatile bool running_ = false;
int relay_gpio_ = 2;
int z_position_steps_ = 0;
int z_max_steps_ = 48000;
int uv_pulse_ms_ = 800;
bool compiling_ = false;

bool readGesture(uint8_t& gesture) {
    Wire.beginTransmission(GESTURE_ADDR);
    Wire.write(0x01);
    if (Wire.endTransmission(false) != 0) {
        return false;
    }
    if (Wire.requestFrom(GESTURE_ADDR, static_cast<uint8_t>(1)) != 1) {
        return false;
    }
    gesture = Wire.read();
    return true;
}

void pulseUv() {
    digitalWrite(relay_gpio_, HIGH);
    vTaskDelay(pdMS_TO_TICKS(uv_pulse_ms_));
    digitalWrite(relay_gpio_, LOW);
}

void pressLoop(void*) {
    pinMode(relay_gpio_, OUTPUT);
    digitalWrite(relay_gpio_, LOW);

    while (running_) {
        uint8_t gesture = 0;
        if (readGesture(gesture)) {
            // PAJ7620 "down" swipe ≈ 0x04 in many M5 examples
            if (gesture == 0x04 && !compiling_) {
                compiling_ = true;
                z_position_steps_ = (z_position_steps_ + 800 < z_max_steps_) ? z_position_steps_ + 800 : z_max_steps_;
                Serial.printf("[HPP] Pull gesture — Z=%d steps\n", z_position_steps_);
                pulseUv();
                compiling_ = false;
            }
        }

        auto* gfx = M5.Display.get();
        if (gfx) {
            gfx->fillRect(0, 0, gfx->width(), 30, TFT_BLACK);
            gfx->setCursor(4, 4);
            gfx->setTextColor(TFT_YELLOW);
            gfx->printf("HPP Z:%d  Pull=Compile", z_position_steps_);
        }
        vTaskDelay(pdMS_TO_TICKS(50));
    }
    vTaskDelete(nullptr);
}

}  // namespace

namespace artifacts {

bool holographic_press_start(const JsonDocument& manifest) {
    JsonVariantConst params = manifest["parameters"];
    if (!params.isNull()) {
        relay_gpio_ = params["relay_gpio"] | 2;
        uv_pulse_ms_ = params["uv_pulse_ms"] | 800;
        int steps_per_mm = params["stepper_steps_per_mm"] | 400;
        int z_max_mm = params["z_max_mm"] | 120;
        z_max_steps_ = steps_per_mm * z_max_mm;
    }

    Wire.begin(M5.Ex_I2C.getSDA(), M5.Ex_I2C.getSCL(), 400000UL);
    running_ = true;
    xTaskCreatePinnedToCore(pressLoop, "hpp_compile", 4096, nullptr, 2, nullptr, 1);
    Serial.println("[HPP] Holographic Printing Press — gesture compiler ready");
    return true;
}

void holographic_press_stop() {
    running_ = false;
    vTaskDelay(pdMS_TO_TICKS(50));
}

}  // namespace artifacts
