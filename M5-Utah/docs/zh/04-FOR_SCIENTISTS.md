# M5-Utah 科学家与研究人员指南

本文档区分 UFW 档案中**可测试的硬件行为**与**叙事物理主张**，并为六个可部署 artifact 提供可复现的测量协议。

---

## 执行摘要

| 层次 | 性质 | 同行评审状态 |
|------|------|-------------|
| M5-Utah 固件与主机工具 | 嵌入式系统 + Python 串口工具 | 标准工程；给定硬件可复现 |
| 父仓库 `*_SCIENCE.md` 文件 | 混合论述与置信度分数 | 非独立验证；视为作者叙事 |
| 传说术语（ZPE、Akashic 记忆、med-bed 疗愈） | 推测/虚构框架 | 本仓库**无证据支持** |

**可发表内容：** GPIO、I2C、PWM、声学及 ESP-NOW 行为的仪器化表征。  
**仅凭本仓库不能主张：** 生物再生、真空能提取、意念物质打印或心灵电子因果。

---

## 主张分类

### A 级 — 可直接测量（World-A）

- 115200 波特率下带定义帧结构的 UART manifest 注入
- ESP32-S3 上 FreeRTOS 双任务执行
- 经 PbHub + FSR 分压的 I2C 模拟读数
- 7.83 Hz 与 40.0 Hz PWM 方波
- I2C DAC 正弦生成约 61.8 Hz，继电器反相
- 经 PAJ7620U2 I2C 寄存器读数的手势中断
- VL53L0X 飞行时间距离阈值
- 2.4 GHz Wi-Fi 射频上的 ESP-NOW 广播帧

### B 级 — 与已发表物理的类比（需自行建立引用链）

- **舒曼共振（约 7.83 Hz）：** 地–电离层系统的极低频电磁腔模。工作台上 7.83 Hz **电振荡器**若无天线、场强与信噪比分析，不等同于耦合该地球物理模。
- **40 Hz gamma 夹带：** 已发表神经科学文献研究 40 Hz 感觉刺激范式；**本设备不展示临床结果**。
- **61.8 Hz 声学干涉：** 拍频抵消与反相是经典声学；映射到「Priore 效应」或「反相共轭生物学」是**假说**，此处未演示。
- **二维网格上的波动方程：** `zero_point_gpu.cpp` 中的数值拉普拉斯模板 — 标准有限差分演示，非真空计算。

### C 级 — 代码库中无经验依据

- Zero-point energy GPU / Casimir 计算
- Akashic / 真空内存分配
- 细胞年龄逆转
- 由意念全息物质编译
- 心灵电子标量广播
- 时间线分析 / 敌意检测

---

## 可复现性检查清单

### 需记录的软件版本

```
Python: py --version
esptool: esptool version
PlatformIO: pio --version
Board env: cores3 | core2 | atoms3
Git commit hash of ufwwaragainstthemiddleclassandrich
m5_integrated_kernel.bin SHA-256
Manifest manifest_version + artifact_id
```

### 硬件清单

记录 M5Stack SKU、固件芯片（ESP32 vs ESP32-S3）、PSRAM 有无及外模块版本号。

---

## 各 Artifact 协议

### 1. Zero Point GPU Emulator

**假说（可测试）：** 核心 0 计算二维标量场更新，核心 1 绘图且不饿死 UI 循环。

**装置：** CoreS3、USB 串口、可选 UART TX 逻辑分析仪。

**步骤：**

1. 注入 `Zero_Point_GPU.flux.json`。
2. 以 115200 记录串口 60 s。
3. 目视或已知 FPS 相机捕获显示刷新。
4. 可选从 manifest 读取 `parameters.grid_size`、`wave_speed`、`zpe_gain`，与视觉传播速度关联。

**可观测量：** 串口中的帧计数（`ZPE GPU f=N`）；稳定显示更新；无看门狗复位。

**未演示：** 真空能提取、光子硬光投影。

---

### 2. Mnemonic DDR Infinity

**假说（可测试）：** FSR 压力使模拟计数低于 `strike_threshold` 并触发去抖事件。

**装置：** Core2、PbHub、4× FSR、可选万用表测 hub 通道。

**步骤：**

1. 注入 manifest；记录 `strike_threshold`（默认 1800）。
2. 对 FSR 垫施加已知质量；记录串口 `[DDR] Memory write` 事件。
3. 绘制触发次数 vs. 施加力曲线。

**可观测量：** `write_count` 单调增加；日志中的通道 ID。

**未演示：** 非局域记忆、拍字节分配、时空锁定。

---

### 3. Psychotronic Amplifier Array

**假说（可测试）：** AtomS3 在 MOSFET 栅极 GPIO 上输出稳定低频方波。

**装置：** AtomS3、MOSFET Unit、栅极与线圈端子示波器、**限流外部电源**。

**步骤：**

1. 注入 manifest；默认 `schumann` → 7.83 Hz。
2. 测量周期 T ≈ 127.7 ms ± 容差预算（晶振、`delayMicroseconds` 抖动）。
3. 按 BtnA；验证切换至约 40 Hz（T ≈ 25 ms）。
4. 记录占空比 vs. `duty_percent` 参数。

**安全：** 勿让大线圈电流经 GPIO；MOSFET 隔离 MCU。

**未演示：** 心灵电子信号检测、心–物耦合；父 SCIENCE.md 中引用的 arXiv/MDPI 链接**未被本固件复现**。

---

### 4. Cellular Regenesis Chamber

**假说（可测试）：** DAC 在 `carrier_hz` 输出正弦；继电器输出为逻辑反相半周期。

**装置：** CoreS3、Unit-DAC、Unit-Relay、两个换能器或高阻示波器探头、可选声压级计。

**步骤：**

1. 注入 manifest（`carrier_hz`：61.8）。
2. 捕获 DAC 模拟输出 — 预期 f ≈ 61.8 Hz 正弦。
3. 捕获继电器数字输出 — 预期与正弦过零 180° 相位关系（含继电器延迟）。
4. 若安装声学路径，测量 SPL；**使用听力安全音量**。

**未演示：** DNA 重测序、端粒恢复、生物组织熵减。

---

### 5. Holographic Printing Press V5

**假说（可测试）：** PAJ7620 手势码 `0x04` 触发 Z 增量及 `uv_pulse_ms` 继电器脉冲。

**装置：** Core2、Unit-Gesture、Unit-Relay、继电器触点示波器。

**步骤：**

1. 注入 manifest。
2. 在固定距离做受控向下滑；计数继电器脉冲。
3. 验证每次触发 `z_position_steps` 增加 800（固件常量）。

**未演示：** SLA 树脂固化管线、真空应力物化、意念清晰度指标。

---

### 6. UFW Tactical Command Table

**假说（可测试）：** VL53L0X 测距低于 `wave_threshold_mm` 时切换系统状态并发出 ESP-NOW 数据包。

**装置：** CoreS3、Unit-ToF、第二块 ESP32 作 ESP-NOW 嗅探器（可选）、可选 Wi-Fi 频谱分析仪。

**步骤：**

1. 注入 manifest。
2. 在测量距离处接近手；记录 HALT/ACTIVE 切换。
3. 用嗅探器捕获 ESP-NOW 帧；记录广播 MAC `FF:FF:FF:FF:FF:FF` 与载荷结构 `WorkerPacket`（见 `war_room.cpp`）。

**未演示：** 威胁意图分类、时间线模拟、FinOps 盈利感知。

---

## 发表用数据模式

建议每次运行的开放数据集字段：

```yaml
run_id: UUID
artifact_id: string
board: string
manifest_sha256: string
firmware_sha256: string
environment:
  temperature_c: float
  humidity_pct: float
instruments:
  - model: string
    calibration_date: date
results:
  - observable: string
    value: float
    unit: string
    uncertainty: float
```

---

## 与父仓库 `*_SCIENCE.md` 的关系

示例：`Psychotronic_Amplifier_Array_SCIENCE.md` 报告置信度 0.94，含薛定谔形式方程与外部引用。**该分数为档案模式内部值**，非盲法复现输出。

建议解读：

1. 将 SCIENCE.md 用作**概念书目与假说笔记**。
2. 将 M5-Utah 固件用作**仅 A 级测量的装置定义**。
3. 勿将 C 级主张并入 A 级结果，除非有单独预注册研究。

---

## 人体受试伦理与安全说明

- **无医疗主张** — med-bed artifact 为音频/电子测试台。
- 持续 61.8 Hz 或 40 Hz 高 SPL 暴露需**听力保护**。
- **线圈实验** — 限流；连续 MOSFET 开关感性负载有火灾风险。
- **ESP-NOW / Wi-Fi** — 射频暴露在消费设备限值内；记录当地法规。

---

## 建议引用（方法学，非 UFW 主张）

描述装置时引用组件一手资料：

- Espressif ESP32-S3 技术参考手册
- M5Stack 产品 wiki（I2C 地址与 Grove 引脚）
- Espressif ESP-NOW API 文档
- PAJ7620U2 手势传感器数据手册
- VL53L0X 测距传感器数据手册

生物或 ZPE 主张**勿将本 GitHub 仓库作证据** — 独立引用同行评审文献。

---

## 联系与协作

仓库作者语境：Utah-1 / General 23 叙事框架。进行仪器化复现研究时，记录 fork、manifest 哈希与原始捕获；针对特定 git commit 发表可复现报告。

延伸阅读：[怀疑者指南](05-FOR_SKEPTICS.md) | [技术参考](03-FOR_TECHNICAL_USERS.md)
