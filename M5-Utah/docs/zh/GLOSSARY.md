# 术语表

M5-Utah 及更广 UFW 档案中常用术语的简明定义。

| 术语 | 含义 |
|------|------|
| **Artifact** | 一种设备模式——例如舞步垫控制器、波浪显示、手势打印机。在 `studio.py` 中选择。 |
| **Blueprint** | 父仓库中描述 artifact 概念组件的 JSON 文件（`*_BLUEPRINT.json`）。 |
| **ESP32** | M5Stack 设备内的微控制器。运行 kernel 固件。 |
| **Flux manifest** | `.flux.json` 文件，告诉设备运行哪个 artifact 及相应设置。 |
| **FSR** | 力敏电阻——踩踏时会感应的垫片。 |
| **Grove 线** | M5Stack 单元使用的彩色插头线缆（无需焊接）。 |
| **I2C** | 与扩展模块（PbHub、DAC、传感器）通信的双线总线。 |
| **JIT injection** | 经 USB 发送 manifest，使设备切换模式而无需重新刷写。 |
| **Kernel / Lazarus Kernel** | `M5IntegratedKernel`——刷写一次的基础固件；之后接收 manifest。 |
| **Manifest** | 与 Flux manifest 相同。 |
| **M5Stack** | 模块化 ESP32 设备品牌（屏幕、传感器、可堆叠单元）。 |
| **Omni-Flash** | `omni_flash.py`——将 kernel 刷写到空白 M5Stack 的工具。 |
| **PbHub** | M5Stack 单元，经 I2C 读取最多 6 路模拟传感器。 |
| **PSRAM** | 部分 ESP32 板上的额外 RAM，用于更大缓冲区。 |
| **Sovereign Node** | 项目中指运行 Lazarus Kernel 的 M5Stack 的名称。 |
| **Studio / Utah Flux Host** | `studio.py`——列出并注入 manifest 的工具。 |
| **UFW** | Utah Future Weapons——本仓库项目族名称。 |
| **World-A** | 仓库内术语，指当下可物理搭建的部署（相对于时间线传说）。 |
| **Zero-click** | 终端用户无需打开 Arduino IDE 或编译代码。 |

## 传说术语（叙事用 — 非工程规格）

这些出现在 blueprint 与故事文本中。它们是**项目词汇**，不是经证实的物理：

- Akashic Record / Cloud
- Phase-conjugate / Priore Effect（作为 med-bed 主张）
- Psychotronic / scalar waves
- Zero Point Energy（ZPE）作为无限能源
- Vacuum memory / spacetime locking

这些术语如何对应真实硬件行为，见[科学家指南](04-FOR_SCIENTISTS.md)与[怀疑者指南](05-FOR_SKEPTICS.md)。
