#include "artifact_runtime.h"

#include <ArduinoJson.h>
#include <cstring>

namespace artifacts {

namespace {
bool active_ = false;
const char* current_id_ = nullptr;

bool zero_point_gpu_start(const JsonDocument&);
void zero_point_gpu_stop();

bool mnemonic_ddr_start(const JsonDocument&);
void mnemonic_ddr_stop();

bool psychotronic_start(const JsonDocument&);
void psychotronic_stop();

bool chrono_heal_start(const JsonDocument&);
void chrono_heal_stop();

bool holographic_press_start(const JsonDocument&);
void holographic_press_stop();

bool war_room_start(const JsonDocument&);
void war_room_stop();

struct Handler {
    const char* id;
    bool (*start)(const JsonDocument&);
    void (*stop)();
};

const Handler kHandlers[] = {
    {"zero_point_gpu", zero_point_gpu_start, zero_point_gpu_stop},
    {"mnemonic_ddr_infinity", mnemonic_ddr_start, mnemonic_ddr_stop},
    {"psychotronic_amplifier_array", psychotronic_start, psychotronic_stop},
    {"cellular_regenesis_chamber", chrono_heal_start, chrono_heal_stop},
    {"holographic_printing_press_v5", holographic_press_start, holographic_press_stop},
    {"ufw_tactical_command_table", war_room_start, war_room_stop},
};

}  // namespace

bool start(const JsonDocument& manifest) {
    stop();

    const char* artifact_id = manifest["artifact_id"] | "";
    if (!artifact_id[0]) {
        Serial.println("[FLUX] Manifest missing artifact_id");
        return false;
    }

    for (const Handler& handler : kHandlers) {
        if (strcmp(handler.id, artifact_id) == 0) {
            if (handler.start(manifest)) {
                active_ = true;
                current_id_ = handler.id;
                Serial.printf("[FLUX] Artifact running: %s\n", handler.id);
                return true;
            }
            return false;
        }
    }

    Serial.printf("[FLUX] Unknown artifact_id: %s\n", artifact_id);
    return false;
}

void stop() {
    if (!active_) {
        return;
    }
    for (const Handler& handler : kHandlers) {
        if (current_id_ && strcmp(handler.id, current_id_) == 0) {
            handler.stop();
            break;
        }
    }
    active_ = false;
    current_id_ = nullptr;
}

bool isRunning() { return active_; }

}  // namespace artifacts
