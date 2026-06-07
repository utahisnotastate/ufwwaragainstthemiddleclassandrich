# 迁移指南：原版 UFW → M5-Utah

本指南面向从**原版档案布局**（27 个项目文件夹、桩代码、手册）起步、迁移到 **M5-Utah**（M5Stack + Flux 部署）的用户。

---

## 一览

| 主题 | 原版（M5 之前） | M5-Utah |
|------|----------------|---------|
| **代码位置** | `ProjectName/Reality_Engine.cpp`、`Matter_Compiler.py` 等 | `M5-Utah/firmware/.../artifacts/*.cpp` + `projects/*.flux.json` |
| **硬件** | 自定义面包板、焊接、Arduino、Pi、CUDA PC | M5Stack Grove 模块，无需焊接 |
| **编译** | 不可编译（虚构 `#include`） | PlatformIO + `build_kernel.ps1` |
| **部署** | 仅概念手册 | 一次 `omni_flash.py`，之后 `studio.py` |
| **切换设备类型** | 每项目重新接线/重编译 | 选择新 `.flux.json` manifest |
| **依赖** | `zpe_core.h`、`scalar_physics` 等（缺失） | M5Unified、ArduinoJson、pyserial |

---

## 各 Artifact 迁移对照

### 1. Zero Point GPU Emulator

| | 原版 | M5-Utah |
|---|------|---------|
| **Blueprint** | `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json` | manifest 中引用同一文件 |
| **代码** | `Reality_Engine.cpp` — `#include <zpe_core.h>`、CUDA 级 PC GPU | `artifacts/zero_point_gpu.cpp` — 2D 波浪数学 + LCD |
| **硬件** | 主机 CPU + 「Casimir Compute Gate」+ HDMI | M5Stack CoreS3 + 可选 DINBase |
| **手册** | `The_Zero_Point_GPU_Emulator_MANUAL.md` — NVIDIA CUDA、16 GB RAM | [非技术用户指南](02-FOR_NON_TECHNICAL_USERS.md) |

**迁移失去：** PC 级渲染叙事。  
**迁移获得：** 便携演示、双核 ESP32、零 CUDA 配置。

---

### 2. Mnemonic DDR Infinity

| | 原版 | M5-Utah |
|---|------|---------|
| **Blueprint** | `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json` | 相同 |
| **代码** | `AKASHIC_RAM.cpp` — `MallocVacuum()`、时空锁定 | `artifacts/mnemonic_ddr.cpp` — PbHub FSR 轮询 |
| **硬件** | DDR5 插槽外形、量子缓存电容（BOM CSV） | Core2 + PbHub + 4× FSR + Grove 线 |
| **手册** | 主板 RAM 槽安装 | FSR 垫下的踩踏板 |

**迁移失去：**「无限拍字节」故事。  
**迁移获得：** 真实踩踏检测，无需压电片齐纳钳位。

---

### 3. Psychotronic Amplifier Array

| | 原版 | M5-Utah |
|---|------|---------|
| **Blueprint** | `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json` | 相同 |
| **科学** | `Psychotronic_Amplifier_Array_SCIENCE.md` | 仍可作为叙事；固件为 PWM |
| **硬件** | 自定义晶体管阵列、蛇杖线圈、石英 — RF 屏蔽关键 | AtomS3 + MOSFET Unit + 线圈接螺丝端子 |
| **代码** | 原版文件夹无 `.cpp` | `artifacts/psychotronic_amplifier.cpp` |

**迁移失去：** 高增益模拟台架搭建。  
**迁移获得：** 隔离 MOSFET 栅极，BtnA 切换 7.83 / 40 Hz。

---

### 4. Cellular Regenesis Chamber

| | 原版 | M5-Utah |
|---|------|---------|
| **Blueprint** | `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json` | 相同 |
| **代码** | `CHRONO_HEAL_KERNEL.cpp` — `PhaseConjugation::invert_time()` | `artifacts/chrono_heal.cpp` — DAC 正弦 + 继电器反相 |
| **硬件** | 运放、特斯拉线圈、面包板寄生风险 | CoreS3 + Unit-DAC + Unit-Relay + 换能器 |
| **手册** | `Cellular_Regenesis_Chamber_MANUAL.md` | Med-bed 声学演示文档 |

**迁移失去：** 反相共轭镜作为生物学的叙事。  
**迁移获得：** 可测量的 61.8 Hz 声学实验。

---

### 5. Holographic Printing Press V5

| | 原版 | M5-Utah |
|---|------|---------|
| **Blueprint** | `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json` | 相同 |
| **代码** | `Matter_Compiler.py` — `scalar_physics`、`consciousness_interface` | `artifacts/holographic_press.cpp` |
| **硬件** | SLA 打印机拆解、Pi GPIO、步进电机改装 | Core2 + Stepmotor Module + Unit-Gesture + Relay |
| **设计文档** | `Holographic Printing Press Design MD.md`（真实 LDGraphy 引用） | 手势上拉 → Z 步进 + UV 脉冲 |

**迁移失去：** 完整树脂 SLA 管线 / G-code。  
**迁移获得：** 无焊手势 + 步进电机堆叠。

---

### 6. UFW Tactical Command Table

| | 原版 | M5-Utah |
|---|------|---------|
| **Blueprint** | `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json` | 相同 |
| **代码** | `REALITY_WAR_ROOM.py` — `timeline_analytics`、`psychotronic_radar` | `artifacts/war_room.cpp` — ESP-NOW + ToF |
| **硬件** | PC 显示器、全息投影、次声低音炮 | CoreS3 overlord + 6× AtomS3 + Unit-ToF |

**迁移失去：** 仅 2D PC 仪表盘。  
**迁移获得：** 物理桌面节点、挥手暂停。

---

## 迁移步骤（检查清单）

### 若你仅使用原版文档 / blueprint

1. 阅读[原版 World-A 方案](07-ORIGINAL_WORLDA_APPROACH.md) — 理解档案曾是什么。
2. 为**一个** artifact 购买 M5 硬件（[Artifact 目录](ARTIFACTS.md)）。
3. `cd M5-Utah` → 安装 `requirements.txt`。
4. 编译或获得 `payloads/m5_integrated_kernel.bin`。
5. `py -3 run_omni_flash.py`（一次）。
6. `py -3 run_studio.py --artifact <id>`，匹配你的板型。
7. 保留原版 `*_BLUEPRINT.json` 作为谱系 — manifest 已链接它们。

### 若你曾尝试编译原版桩代码

1. **停止**追寻 `zpe_core.h`、`vacuum_dynamics.h`、`scalar_physics` — 它们不在仓库中。
2. 仅将**逻辑思路**（如步进检测、频率值）移植到 `.flux.json` 的 M5 artifact 参数。
3. 真实实现在 `M5-Utah/firmware/M5IntegratedKernel/src/artifacts/`。

### 若你已焊接原版 World-A 面包板

可**同时运行**：原版台架做实验；M5-Utah 做演示与教学。二者不互斥。记录哪套物理搭建对应哪套文档。

---

## 文件路径速查

```
ORIGINAL                          M5-UTAH
────────────────────────────────  ────────────────────────────────────
README.md (UFW lore)              M5-Utah/README.md (deploy)
Project/Project_BLUEPRINT.json    projects/Artifact.flux.json
Project/foo.cpp (stub)            firmware/.../artifacts/foo.cpp
Project/Project_MANUAL.md         docs/zh/02-FOR_NON_TECHNICAL_USERS.md
(none)                            host/studio.py, omni_flash.py
(none)                            payloads/m5_integrated_kernel.bin
```

---

## 常见问题

**要删除 27 个原版文件夹吗？**  
不。它们仍是概念档案。M5-Utah 是硬件部署层。

**迁移会改变故事/传说吗？**  
不会。时间线叙事仍在父 README 与 `*_SCIENCE.md`。M5-Utah 文档诚实说明 World-A 行为。

**能添加第 7 个 artifact 吗？**  
扩展 `artifact_runtime.cpp`，添加 `projects/NewThing.flux.json`，重新编译 kernel。原版模式是仅添加新的顶层文件夹。

---

## 另见

- [原版 World-A 方案](07-ORIGINAL_WORLDA_APPROACH.md)
- [技术参考](03-FOR_TECHNICAL_USERS.md)
- [Artifact 目录](ARTIFACTS.md)
