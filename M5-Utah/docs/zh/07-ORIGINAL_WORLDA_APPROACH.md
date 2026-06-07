# 原版 World-A 方案（M5Stack 之前）

在 **M5-Utah** 出现之前，UFW 仓库组织为**扁平的 27 个项目档案**。本文档描述该原版布局，便于与 M5 迁移路径对照。

---

## 仓库结构（原版）

```
ufwwaragainstthemiddleclassandrich/
├── README.md
├── The_Zero_Point_GPU_Emulator/
│   ├── The_Zero_Point_GPU_Emulator_BLUEPRINT.json
│   ├── The_Zero_Point_GPU_Emulator_MANUAL.md
│   ├── The_Zero_Point_GPU_Emulator_SCIENCE.md
│   ├── Reality_Engine.cpp          ← 桩代码，不可编译
│   └── The_Zero_Point_GPU_Emulator_LANDING.html
├── Mnemonic_DDR_Infinity/
│   ├── Mnemonic_DDR_Infinity_BLUEPRINT.json
│   ├── Mnemonic_DDR_Infinity_BOM.csv
│   ├── AKASHIC_RAM.cpp
│   └── ...
├── ... (另有 25 个项目，模式相同)
└── (无 M5-Utah/，无构建系统)
```

每个项目通常包含：

| 文件类型 | 用途 |
|----------|------|
| `*_BLUEPRINT.json` | 组件图 / 几何树 |
| `*_SCIENCE.md` | 验证叙事、方程、mermaid |
| `*_MANUAL.md` | 安装与操作说明 |
| `*_3D.json` | 场景元数据 |
| `*_LANDING.html` | 静态宣传页 |
| `*.cpp` / `*.py` | 带**虚构 import** 的概念代码 |

当时**没有** `requirements.txt`、PlatformIO 或统一刷写工具。

---

## 原版应如何搭建（原版规格）

Batch 1–2 设计简报（M5 迁移前）描述**手工搭建的 World-A** 台架：

### Zero Point GPU
- **软件路径：** 在 **CUDA 级 PC** 上针对真空/GPU 库编译 `Reality_Engine.cpp`。
- **手册写明：** NVIDIA GPU、16 GB RAM、GCC、CUDA Toolkit。
- **现实：** 仓库中不存在 `zpe_core.h`。

### Mnemonic DDR Infinity
- **硬件路径：** DDR5 内存条外形，或在 **Arduino** 上使用压电踩踏片。
- **问题：** 自定义电压钳位（齐纳、下拉）、面包板噪声。
- **BOM CSV：** 真实零件（Kingston DDR、Murata 电容）与虚构「量子缓存」混合。

### Psychotronic Amplifier Array
- **硬件路径：** 手焊高增益晶体管、蛇杖线圈、石英谐振器。
- **问题：** 无仔细屏蔽时的 RF 噪声（「光子猝灭」）。
- **文档：** `Psychotronic_Amplifier_Array_SCIENCE.md`（置信度 0.94）— 叙事，非固件。

### Cellular Regenesis Chamber
- **硬件路径：** 外露运放、自定义特斯拉线圈、面包板上的反相共轭镜。
- **代码：** `CHRONO_HEAL_KERNEL.cpp` → `#include <phase_conjugation.h>`（缺失）。
- **另有：** `Telomere_Restore.cpp`、OpenSCAD 舱体几何。

### Holographic Printing Press V5
- **硬件路径：** 经 **Raspberry Pi GPIO** 逆向 **SLA 3D 打印机**电机驱动。
- **软件：** `Matter_Compiler.py` → `scalar_physics`、`consciousness_interface`（缺失）。
- **真实工程：** `Holographic Printing Press Design MD.md` 引用 LDGraphy 风格设计。

### UFW Tactical Command Table
- **硬件路径：** PC 显示器「上帝之眼」仪表盘。
- **软件：** `REALITY_WAR_ROOM.py` → `timeline_analytics`、`psychotronic_radar`（缺失）。
- **局限：** 仅 2D 屏幕；无物理集群节点。

---

## 原版工作流（典型用户）

1. 克隆仓库，打开某项目文件夹。
2. 阅读 `*_MANUAL.md` 与 `*_BLUEPRINT.json`。
3. 尝试编译 `*.cpp` 或运行 `*.py` → 因缺失模块**失败**。
4. 可选：根据 BOM / 科学文档搭建**受启发**的面包板。
5. 阅读根 `README.md` 了解 UFW 经济/时间线叙事。

**验证叙事：** 根 README 中的「可用代码」指**概念上**可用的 blueprint，而非单一可运行二进制。

---

## 原版 vs M5-Utah（摘要）

| 维度 | 原版 World-A | M5-Utah |
|------|-------------|---------|
| **组装** | 焊接、接线、钳压 | Grove 线、螺丝端子 |
| **工具链** | Arduino IDE、每项目 PlatformIO、CUDA、Pi | 单一 kernel + manifest 注入 |
| **代码状态** | 桩代码 + 传说 | 可编译固件 + Python 主机 |
| **项目数量** | 27 个档案 | 6 个已部署 artifact（更多计划中） |
| **用户技能** | 电子工程 + 软件 | 插 USB、选列表 |
| **Blueprint 角色** | 主要规格 | `.flux.json` 中链接的谱系 |
| **诚实演示** | 需自行解读 | 科学家/怀疑者指南中已文档化 |

---

## 今日何时使用原版文档

| 使用原版 | 使用 M5-Utah |
|----------|-------------|
| 传说、科幻、引用 | 实际刷写硬件 |
| OpenSCAD / 3D 几何 | 桌面舞步垫、波浪、手势 |
| 完整 27 项目目录 | 六个 MVP artifact |
| 撰写关于**叙事**的论文 | 仪器化**测量**协议 |

---

## 向前迁移

分步从原版文件夹转换到 M5-Utah manifest，见 **[迁移指南](06-MIGRATION_FROM_ORIGINAL.md)**。

---

## 另见

- [文档中心](README.md)
- [Artifact 目录](ARTIFACTS.md) — M5 BOM 与 blueprint 路径对照
- 父仓库 `README.md` — 未改的 UFW 使命陈述
