#pragma once

#include <ArduinoJson.h>

namespace artifacts {

bool start(const JsonDocument& manifest);
void stop();
bool isRunning();

}  // namespace artifacts
