# M5-Utah 非技术用户指南

你**不需要**编程、焊接或打开 Arduino IDE。只要能插 USB 线、双击程序（或运行朋友给你的命令），就能使用本系统。

---

## 你会得到什么

**M5-Utah** 把小型 M5Stack 设备变成多种实用装置：

- 用于舞蹈或健身游戏的**舞步垫控制器**
- **彩色显示演示**（波浪模拟器）
- 用于线圈实验的**低频振荡器**
- 带双路输出的**声波演示**
- **手势控制电机演示**
- 响应挥手的**桌面仪表盘**

硬件只需买一次、刷写一次，之后随时从列表中选名称即可**切换模式**。

---

## 购买清单（入门套件）

先选**一个**项目入门。所有项目共用同一套基础软件。

### 最简单入门：波浪画板（仅 CoreS3）

| 物品 | 大致用途 |
|------|---------|
| M5Stack CoreS3 | 带屏幕的主设备 |
| USB-C 线 | 通常随设备附带 |

### 舞步垫：Mnemonic DDR

| 物品 | 数量 |
|------|------|
| M5Stack Core2 | 1 |
| M5Stack PbHub Unit | 1 |
| M5Stack FSR Unit | 4 |
| Grove 线（HY2.0-4P） | 5 |

### 完整清单

每个 BOM 见 [Artifact 目录](ARTIFACTS.md)。

---

## 一次性设置（请技术朋友帮忙，或严格按步骤操作）

### 在电脑上

1. 从 [python.org](https://www.python.org/downloads/) 安装 **Python 3**（Windows 上勾选「Add to PATH」）。
2. 在 `M5-Utah` 文件夹中打开终端。
3. 运行：
   ```
   py -3 -m pip install -r requirements.txt
   ```
4. 若你已收到预编译的 `m5_integrated_kernel.bin`，它应在 `M5-Utah/payloads/` 中。若没有，需技术朋友编译（见[技术指南](03-FOR_TECHNICAL_USERS.md)）。

### 在 M5Stack 上（仅首次）

1. 用 USB-C 将 M5Stack 连到电脑。
2. 运行：
   ```
   py -3 run_omni_flash.py
   ```
3. 等待 **SUCCESS**。设备现已成为空白「接收器」。

**除非换新板或重大固件更新，否则只需刷写一次**。

---

## 日常使用（每次想换设备模式时）

1. 插上 USB-C。
2. 运行：
   ```
   py -3 run_studio.py
   ```
3. 你会看到编号列表，例如：
   ```
   [0] Cellular_Regenesis_Chamber.flux.json  (Med-Bed / cores3)
   [1] Holographic_Printing_Press_V5.flux.json  ...
   ...
   ```
4. 输入数字并按 Enter。
5. M5Stack 重启进入该模式。完成。

### 快捷方式（若有人给了你名称）

```
py -3 run_studio.py --artifact mnemonic_ddr_infinity
```

### 不插设备时列出模式

```
py -3 run_studio.py --list
```

---

## 物理组装（无需焊接）

所有 M5Stack 单元使用 **Grove 线**——彩色插头，咔嗒一声即可插入。

**示例 — 舞步垫：**

1. 将 **PbHub** 插入 Core2 的 **Port A**（红色）。
2. 将每个 **FSR** 插入 PbHub 的 **CH0、CH1、CH2、CH3**。
3. 将每个 FSR 放在地板板或纸板「踩踏区」下方。

**示例 — Med-Bed 声音演示：**

1. 将 **Unit-DAC** 插入 CoreS3 的 Port A。
2. 将 **Unit-Relay** 插入 Port B。
3. 将小扬声器或激振器接到螺丝端子（需成人协助）。

图示与端口名称：[Artifact 目录](ARTIFACTS.md)。

---

## 如何确认正常工作

| 设备模式 | 你应该看到… |
|----------|------------|
| 波浪画板 | 屏幕上颜色在动 |
| 舞步记忆 | 踩垫时数字增加 |
| 嗡嗡盒 | AtomS3 屏幕显示状态；线圈经 MOSFET 驱动（不确定时用示波器或线圈上的 LED） |
| Med-Bed 演示 | 串口消息；若已接线则有换能器声音 |
| 手势打印机 | 在手势传感器前向下滑时 Z 高度数字增加 |
| 作战桌 | 在 ToF 传感器上方挥手时屏幕显示 ACTIVE 或 HALT |

若无反应：见下方**故障排除**。

---

## 故障排除

| 问题 | 尝试 |
|------|------|
| 「No M5Stack detected」 | 换 USB 线；换 USB 口；安装 CP210x 或 CH340 驱动（搜索板名 + 「USB driver」） |
| 刷写失败 | 插 USB 时按住 **BOOT**，再重试 `run_omni_flash.py` |
| 注入后模式错误 | 拔插 USB，用正确编号重新运行 `run_studio.py` |
| 舞步垫无反应 | 检查 Grove 线是否插紧；PbHub 是否在 Port A |
| 屏幕空白 | 重新刷写 kernel；确认针对正确板型编译/刷写（Core2 vs CoreS3 vs AtomS3） |

---

## 这不是什么

说清楚对大家都好：

- **不是**医疗设备。「Med-Bed」是**音频频率演示**。
- **不是**真正的全息打印机。它是**手势 + 电机 + 继电器演示**。
- **不是**无限计算机内存。舞步模式**记录踩踏事件**。
- **不是**经证实的「心灵电子」技术。它在 GPIO 引脚输出**已知频率**（7.83 Hz、40 Hz）。

**故事与名称**来自 UFW 创意档案。**硬件行为**是普通电子，可用眼睛和耳朵验证。

更多细节：[怀疑者指南](05-FOR_SKEPTICS.md)

---

## 原版 UFW 与 M5（该读哪份文档？）

| 情况 | 阅读 |
|------|------|
| 你有**旧的 27 文件夹**仓库布局 | [原版 World-A 方案](07-ORIGINAL_WORLDA_APPROACH.md) |
| 你正从面包板/Arduino **切换**到 M5 | [迁移指南](06-MIGRATION_FROM_ORIGINAL.md) |

## 获取帮助

| 需求 | 阅读 |
|------|------|
| 儿童友好说明 | [儿童指南](01-FOR_CHILDREN.md) |
| 自行编译固件 | [技术用户指南](03-FOR_TECHNICAL_USERS.md) |
| 测量与引用实验 | [科学家指南](04-FOR_SCIENTISTS.md) |
| 所有零件名称 | [术语表](GLOSSARY.md) |
