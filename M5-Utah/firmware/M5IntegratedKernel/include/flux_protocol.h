#pragma once

#include <ArduinoJson.h>
#include <stdint.h>

namespace flux {

constexpr char SYNC_START[] = "FLUX_SYNC_START";
constexpr char SYNC_END[] = "FLUX_SYNC_END";
constexpr size_t MAX_MANIFEST_BYTES = 8192;

enum class RxState {
    Idle,
    Header,
    Size,
    Payload,
    Footer,
};

class Protocol {
public:
    void begin();
    bool poll(Stream& serial);
    bool hasManifest() const { return manifest_ready_; }
    const JsonDocument& manifest() const { return doc_; }
    void clear();

private:
    RxState state_ = RxState::Idle;
    uint8_t header_idx_ = 0;
    uint8_t footer_idx_ = 0;
    uint32_t expected_size_ = 0;
    uint32_t received_size_ = 0;
    bool manifest_ready_ = false;
    char buffer_[MAX_MANIFEST_BYTES] = {};
    StaticJsonDocument<MAX_MANIFEST_BYTES> doc_;

    bool matchHeader(char c);
    bool matchFooter(char c);
    bool parseManifest();
};

}  // namespace flux
