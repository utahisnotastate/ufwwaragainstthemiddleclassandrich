#include <M5Unified.h>
#include <ArduinoJson.h>
#include <math.h>

namespace {

TaskHandle_t compute_task_ = nullptr;
TaskHandle_t display_task_ = nullptr;
volatile bool running_ = false;

int grid_size_ = 32;
float wave_speed_ = 0.15f;
float zpe_gain_ = 1.618f;
float* field_ = nullptr;
uint32_t frame_ = 0;

void computeLoop(void*) {
    const int n = grid_size_ * grid_size_;
    while (running_) {
        for (int i = 1; i < grid_size_ - 1; ++i) {
            for (int j = 1; j < grid_size_ - 1; ++j) {
                int idx = i * grid_size_ + j;
                float lap =
                    field_[idx - 1] + field_[idx + 1] + field_[idx - grid_size_] + field_[idx + grid_size_] -
                    4.0f * field_[idx];
                field_[idx] += wave_speed_ * lap * zpe_gain_;
            }
        }
        if ((frame_++ % 4) == 0) {
            int cx = grid_size_ / 2;
            field_[cx * grid_size_ + cx] = sinf(frame_ * 0.05f) * 0.5f + 0.5f;
        }
        vTaskDelay(pdMS_TO_TICKS(16));
    }
    vTaskDelete(nullptr);
}

void displayLoop(void*) {
    while (running_) {
        auto* gfx = M5.Display.get();
        if (!gfx) {
            vTaskDelay(pdMS_TO_TICKS(100));
            continue;
        }
        int w = gfx->width();
        int h = gfx->height();
        int cell_w = w / grid_size_;
        int cell_h = h / grid_size_;

        for (int y = 0; y < grid_size_; ++y) {
            for (int x = 0; x < grid_size_; ++x) {
                float v = field_[y * grid_size_ + x];
                v = constrain(v, 0.0f, 1.0f);
                uint8_t r = static_cast<uint8_t>(v * 80);
                uint8_t g = static_cast<uint8_t>(v * 200);
                uint8_t b = static_cast<uint8_t>((1.0f - v) * 255);
                gfx->fillRect(x * cell_w, y * cell_h, cell_w, cell_h, gfx->color888(r, g, b));
            }
        }
        gfx->setCursor(4, 4);
        gfx->setTextColor(TFT_WHITE);
        gfx->printf("ZPE GPU f=%lu", static_cast<unsigned long>(frame_));
        vTaskDelay(pdMS_TO_TICKS(33));
    }
    vTaskDelete(nullptr);
}

}  // namespace

namespace artifacts {

bool zero_point_gpu_start(const JsonDocument& manifest) {
    JsonVariantConst params = manifest["parameters"];
    if (!params.isNull()) {
        grid_size_ = params["grid_size"] | 32;
        wave_speed_ = params["wave_speed"] | 0.15f;
        zpe_gain_ = params["zpe_gain"] | 1.618f;
    }

    const int n = grid_size_ * grid_size_;
    field_ = static_cast<float*>(heap_caps_malloc(n * sizeof(float), MALLOC_CAP_SPIRAM | MALLOC_CAP_8BIT));
    if (!field_) {
        field_ = static_cast<float*>(malloc(n * sizeof(float)));
    }
    if (!field_) {
        Serial.println("[ZPE] Field allocation failed");
        return false;
    }
    for (int i = 0; i < n; ++i) {
        field_[i] = 0.0f;
    }

    running_ = true;
    xTaskCreatePinnedToCore(computeLoop, "reality_engine", 4096, nullptr, 2, &compute_task_, 0);
    xTaskCreatePinnedToCore(displayLoop, "voxel_display", 8192, nullptr, 1, &display_task_, 1);
    Serial.println("[ZPE] Reality Engine online — Core0 compute / Core1 display");
    return true;
}

void zero_point_gpu_stop() {
    running_ = false;
    vTaskDelay(pdMS_TO_TICKS(100));
    if (field_) {
        free(field_);
        field_ = nullptr;
    }
    compute_task_ = nullptr;
    display_task_ = nullptr;
}

}  // namespace artifacts
