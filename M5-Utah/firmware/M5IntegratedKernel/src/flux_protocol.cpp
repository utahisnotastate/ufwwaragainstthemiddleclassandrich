#include "flux_protocol.h"

#include <cstring>

namespace flux {

void Protocol::begin() {
    clear();
}

void Protocol::clear() {
    state_ = RxState::Idle;
    header_idx_ = 0;
    footer_idx_ = 0;
    expected_size_ = 0;
    received_size_ = 0;
    manifest_ready_ = false;
    std::memset(buffer_, 0, sizeof(buffer_));
    doc_.clear();
}

bool Protocol::matchHeader(char c) {
    if (c == SYNC_START[header_idx_]) {
        header_idx_++;
        if (header_idx_ >= sizeof(SYNC_START) - 1) {
            state_ = RxState::Size;
            header_idx_ = 0;
            return true;
        }
    } else {
        header_idx_ = (c == SYNC_START[0]) ? 1 : 0;
    }
    return false;
}

bool Protocol::matchFooter(char c) {
    if (c == SYNC_END[footer_idx_]) {
        footer_idx_++;
        if (footer_idx_ >= sizeof(SYNC_END) - 1) {
            footer_idx_ = 0;
            return true;
        }
    } else {
        footer_idx_ = (c == SYNC_END[0]) ? 1 : 0;
    }
    return false;
}

bool Protocol::parseManifest() {
    DeserializationError err = deserializeJson(doc_, buffer_, received_size_);
    if (err) {
        Serial.printf("[FLUX] JSON parse error: %s\n", err.c_str());
        clear();
        return false;
    }
    manifest_ready_ = true;
    state_ = RxState::Idle;
    return true;
}

bool Protocol::poll(Stream& serial) {
    while (serial.available()) {
        char c = static_cast<char>(serial.read());

        switch (state_) {
            case RxState::Idle:
                matchHeader(c);
                break;

            case RxState::Size: {
                static uint8_t size_buf[4] = {};
                static uint8_t size_idx = 0;
                size_buf[size_idx++] = static_cast<uint8_t>(c);
                if (size_idx >= 4) {
                    expected_size_ = static_cast<uint32_t>(size_buf[0]) |
                                     (static_cast<uint32_t>(size_buf[1]) << 8) |
                                     (static_cast<uint32_t>(size_buf[2]) << 16) |
                                     (static_cast<uint32_t>(size_buf[3]) << 24);
                    size_idx = 0;
                    received_size_ = 0;
                    if (expected_size_ == 0 || expected_size_ >= MAX_MANIFEST_BYTES) {
                        Serial.println("[FLUX] Invalid payload size");
                        clear();
                    } else {
                        state_ = RxState::Payload;
                    }
                }
                break;
            }

            case RxState::Payload:
                if (received_size_ < expected_size_) {
                    buffer_[received_size_++] = c;
                }
                if (received_size_ >= expected_size_) {
                    state_ = RxState::Footer;
                    footer_idx_ = 0;
                }
                break;

            case RxState::Footer:
                if (matchFooter(c)) {
                    return parseManifest();
                }
                break;

            default:
                clear();
                break;
        }
    }
    return false;
}

}  // namespace flux
