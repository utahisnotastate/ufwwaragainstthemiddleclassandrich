# Artifact 目录

六个 UFW artifact 现可通过 M5-Utah 部署。每行列出**购买清单**、**在 World-A 中设备实际做什么**，以及**原始 blueprint 位置**。

## 总览表

| # | 名称 | M5 板型 | 扩展模块 | World-A 行为 |
|---|------|---------|----------|-------------|
| 1 | Zero Point GPU Emulator | CoreS3 | DINBase（可选散热） | 屏幕上的动画波浪网格；一核算数学，另一核绘图 |
| 2 | Mnemonic DDR Infinity | Core2 | PbHub + 4× FSR + Grove 线 | 舞步垫触发「memory write」事件；屏幕显示计数 |
| 3 | Psychotronic Amplifier Array | AtomS3 | MOSFET Unit + 手绕线圈 | 7.83 Hz 或 40 Hz PWM 振荡器；外部电源驱动线圈 |
| 4 | Cellular Regenesis Chamber | CoreS3 | Unit-DAC + Unit-Relay + 换能器 | DAC 输出 61.8 Hz 正弦；继电器反相用于声学实验 |
| 5 | Holographic Printing Press V5 | Core2 | Stepmotor + Unit-Gesture + Unit-Relay | 检测到手势下滑 → Z 步进计数 + UV 继电器脉冲（演示） |
| 6 | UFW Tactical Command Table | CoreS3 | Unit-ToF + 6× AtomS3 Lite（集群） | ESP-NOW 广播；ToF 挥手切换 halt/execute（overlord 节点） |

## 各 Artifact 详情

### 1. Zero Point GPU Emulator

- **Manifest：** `projects/Zero_Point_GPU.flux.json`
- **Blueprint：** `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json`
- **源桩代码：** `The_Zero_Point_GPU_Emulator/Reality_Engine.cpp`
- **组装：** CoreS3 卡入 DINBase；USB-C 连电脑。
- **验证：** 屏幕显示实时彩色网格；串口打印帧更新。

### 2. Mnemonic DDR Infinity（舞步机）

- **Manifest：** `projects/Mnemonic_DDR_Infinity.flux.json`
- **Blueprint：** `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json`
- **源桩代码：** `Mnemonic_DDR_Infinity/AKASHIC_RAM.cpp`
- **组装：** PbHub 接 Port A；FSR 接 CH0–CH3；安装在踩踏板下方。
- **验证：** 踩垫 → 串口记录 `[DDR] Memory write`；屏幕计数增加。

### 3. Psychotronic Amplifier Array（PAA）

- **Manifest：** `projects/Psychotronic_Amplifier_Array.flux.json`
- **Blueprint：** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json`
- **科学文档：** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_SCIENCE.md`
- **组装：** MOSFET 接 Port A；线圈引线接螺丝端子；**线圈电流使用外部电源**。
- **验证：** 示波器测 MOSFET 输出为约 7.83 Hz 或 40 Hz 方波；按 AtomS3 的 BtnA 切换模式。

### 4. Cellular Regenesis Chamber（Med-Bed）

- **Manifest：** `projects/Cellular_Regenesis_Chamber.flux.json`
- **Blueprint：** `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json`
- **源桩代码：** `Cellular_Regenesis_Chamber/CHRONO_HEAL_KERNEL.cpp`
- **组装：** Unit-DAC 接 Port A；Unit-Relay 接 Port B；音频换能器接端子。
- **验证：** DAC 输出正弦；继电器在半周期反相切换；串口记录 `[CHRONO]`。

### 5. Holographic Printing Press V5

- **Manifest：** `projects/Holographic_Printing_Press_V5.flux.json`
- **Blueprint：** `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json`
- **源桩代码：** `Holographic_Printing_Press_V5/Matter_Compiler.py`
- **组装：** Stepmotor 叠在 Core2 下；Gesture 接 A；Relay 接 B；NEMA-17 接步进端子。
- **验证：** 手势传感器向下滑动使 Z 增加并脉冲继电器（UV 演示）。

### 6. UFW Tactical Command Table

- **Manifest：** `projects/UFW_Tactical_Command_Table.flux.json`
- **Blueprint：** `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json`
- **源桩代码：** `UFW_Tactical_Command_Table/REALITY_WAR_ROOM.py`
- **组装：** CoreS3 居中；Unit-ToF 接 Port A；可选 6× AtomS3 Lite worker 用于 ESP-NOW 集群。
- **验证：** 手进入 ToF 范围时屏幕切换 HALT/ACTIVE；串口监视器可见 ESP-NOW 数据包。

## 注入命令

```bash
py -3 run_studio.py --artifact zero_point_gpu
py -3 run_studio.py --artifact mnemonic_ddr_infinity
py -3 run_studio.py --artifact psychotronic_amplifier_array
py -3 run_studio.py --artifact cellular_regenesis_chamber
py -3 run_studio.py --artifact holographic_printing_press_v5
py -3 run_studio.py --artifact ufw_tactical_command_table
```
