# Каталог артефактов

Шесть артефактов UFW развёртываются сегодня через M5-Utah. Каждая строка перечисляет **что купить**, **что устройство реально делает в World-A** и **где живёт оригинальный blueprint**.

## Сводная таблица

| # | Название | Плата M5 | Дополнения | Поведение World-A |
|---|----------|----------|------------|-------------------|
| 1 | Zero Point GPU Emulator | CoreS3 | DINBase (опционально охлаждение) | Анимированная волновая сетка на экране; математика на одном ядре CPU, отрисовка на другом |
| 2 | Mnemonic DDR Infinity | Core2 | PbHub + 4× FSR + Grove-кабели | Ступенчатые площадки вызывают события «memory write»; счётчики на дисплее |
| 3 | Psychotronic Amplifier Array | AtomS3 | MOSFET Unit + ручная катушка | ШИМ-осциллятор на 7.83 Hz или 40 Hz; внешний БП питает катушку |
| 4 | Cellular Regenesis Chamber | CoreS3 | Unit-DAC + Unit-Relay + излучатели | 61.8 Hz синус на DAC; инвертированная фаза на реле для акустических экспериментов |
| 5 | Holographic Printing Press V5 | Core2 | Stepmotor + Unit-Gesture + Unit-Relay | Обнаружен свайп рукой → счётчик шагов Z + импульс УФ-реле (демо) |
| 6 | UFW Tactical Command Table | CoreS3 | Unit-ToF + 6× AtomS3 Lite (swarm) | Широковещание ESP-NOW; взмах рукой ToF переключает halt/execute (overlord node) |

## Детали по артефактам

### 1. Zero Point GPU Emulator

- **Manifest:** `projects/Zero_Point_GPU.flux.json`
- **Blueprint:** `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json`
- **Source stub:** `The_Zero_Point_GPU_Emulator/Reality_Engine.cpp`
- **Сборка:** Установите CoreS3 на DINBase; USB-C к ПК.
- **Проверка:** На экране живая цветная сетка; serial выводит обновления кадров.

### 2. Mnemonic DDR Infinity (Step Machine)

- **Manifest:** `projects/Mnemonic_DDR_Infinity.flux.json`
- **Blueprint:** `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json`
- **Source stub:** `Mnemonic_DDR_Infinity/AKASHIC_RAM.cpp`
- **Сборка:** PbHub на Port A; FSR на CH0–CH3; установите под ступенчатыми пластинами.
- **Проверка:** Наступление на площадку → serial логирует `[DDR] Memory write`; счётчик на экране увеличивается.

### 3. Psychotronic Amplifier Array (PAA)

- **Manifest:** `projects/Psychotronic_Amplifier_Array.flux.json`
- **Blueprint:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json`
- **Science doc:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_SCIENCE.md`
- **Сборка:** MOSFET на Port A; выводы катушки в винтовых клеммах; **используйте внешний БП для тока катушки**.
- **Проверка:** Осциллограф на выходе MOSFET показывает ~7.83 Hz или 40 Hz прямоугольную волну; нажмите BtnA на AtomS3 для переключения режима.

### 4. Cellular Regenesis Chamber (Med-Bed)

- **Manifest:** `projects/Cellular_Regenesis_Chamber.flux.json`
- **Blueprint:** `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json`
- **Source stub:** `Cellular_Regenesis_Chamber/CHRONO_HEAL_KERNEL.cpp`
- **Сборка:** Unit-DAC на Port A; Unit-Relay на Port B; акустические излучатели на клеммных блоках.
- **Проверка:** DAC выводит синус; реле переключается при инверсии полупериода; serial логирует `[CHRONO]`.

### 5. Holographic Printing Press V5

- **Manifest:** `projects/Holographic_Printing_Press_V5.flux.json`
- **Blueprint:** `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json`
- **Source stub:** `Holographic_Printing_Press_V5/Matter_Compiler.py`
- **Сборка:** Stepmotor под Core2; Gesture на A; Relay на B; NEMA-17 на клеммах stepper.
- **Проверка:** Свайп вниз на датчике жестов увеличивает Z и импульсирует реле (УФ-демо).

### 6. UFW Tactical Command Table

- **Manifest:** `projects/UFW_Tactical_Command_Table.flux.json`
- **Blueprint:** `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json`
- **Source stub:** `UFW_Tactical_Command_Table/REALITY_WAR_ROOM.py`
- **Сборка:** CoreS3 в центре; Unit-ToF на Port A; опционально 6× AtomS3 Lite workers для ESP-NOW swarm.
- **Проверка:** Рука в зоне ToF переключает HALT/ACTIVE на экране; пакеты ESP-NOW в serial monitor.

## Команды инъекции

```bash
py -3 run_studio.py --artifact zero_point_gpu
py -3 run_studio.py --artifact mnemonic_ddr_infinity
py -3 run_studio.py --artifact psychotronic_amplifier_array
py -3 run_studio.py --artifact cellular_regenesis_chamber
py -3 run_studio.py --artifact holographic_printing_press_v5
py -3 run_studio.py --artifact ufw_tactical_command_table
```
