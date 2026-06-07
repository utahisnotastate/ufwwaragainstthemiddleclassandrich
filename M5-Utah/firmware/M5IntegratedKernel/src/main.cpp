#include <M5Unified.h>

#include "artifact_runtime.h"
#include "flux_protocol.h"

flux::Protocol g_flux;

void printBanner() {
    Serial.println();
    Serial.println("=== M5IntegratedKernel / Lazarus Receiver ===");
    Serial.println("Utah Flux JIT substrate ready.");
    Serial.printf("Board: %s\n", M5.getBoardName());
    Serial.println("Awaiting .flux.json manifest via serial...");
    Serial.println();
}

void setup() {
    auto cfg = M5.config();
    M5.begin(cfg);
    Serial.begin(115200);
    delay(500);

    printBanner();
    g_flux.begin();
}

void loop() {
    M5.update();

    if (g_flux.poll(Serial)) {
        Serial.println("[FLUX] Manifest received");
        const JsonDocument& manifest = g_flux.manifest();
        const char* name = manifest["display_name"] | "unknown";
        Serial.printf("[FLUX] Manifesting: %s\n", name);

        if (artifacts::start(manifest)) {
            Serial.println("[FLUX] ACK: ARTIFACT_ACTIVE");
        } else {
            Serial.println("[FLUX] ACK: ARTIFACT_FAILED");
        }
        g_flux.clear();
    }

    delay(10);
}
