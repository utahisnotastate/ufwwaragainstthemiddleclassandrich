# Руководство по миграции: оригинальный UFW → M5-Utah

Это руководство для тех, кто начинал с **оригинальной структуры архива** (27 папок проектов, заглушки, мануалы) и переходит на **M5-Utah** (M5Stack + развёртывание Flux).

---

## Краткий обзор

| Тема | Оригинал (до M5) | M5-Utah |
|------|------------------|---------|
| **Где живёт код** | `ProjectName/Reality_Engine.cpp`, `Matter_Compiler.py` и т.д. | `M5-Utah/firmware/.../artifacts/*.cpp` + `projects/*.flux.json` |
| **Оборудование** | Самодельные макеты, пайка, Arduino, Pi, CUDA ПК | Модули M5Stack Grove, без пайки |
| **Сборка** | Не собирается (вымышленные `#include`) | PlatformIO + `build_kernel.ps1` |
| **Развёртывание** | Только концептуальные мануалы | `omni_flash.py` один раз, затем `studio.py` |
| **Смена типа устройства** | Перепроводка / перекомпиляция на проект | Выбор нового манифеста `.flux.json` |
| **Зависимости** | `zpe_core.h`, `scalar_physics` и т.д. (отсутствуют) | M5Unified, ArduinoJson, pyserial |

---

## Карта миграции по артефактам

### 1. Zero Point GPU Emulator

| | Оригинал | M5-Utah |
|---|----------|---------|
| **Blueprint** | `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json` | Тот же файл, на который ссылается манифест |
| **Код** | `Reality_Engine.cpp` — `#include <zpe_core.h>`, CUDA-класс GPU ПК | `artifacts/zero_point_gpu.cpp` — 2D волновая математика + LCD |
| **Оборудование** | CPU хоста + «Casimir Compute Gate» + HDMI | M5Stack CoreS3 + опционально DINBase |
| **Мануал** | `The_Zero_Point_GPU_Emulator_MANUAL.md` — NVIDIA CUDA, 16 GB RAM | [Для нетехнических пользователей](02-FOR_NON_TECHNICAL_USERS.md) |

**Что теряете при миграции:** Нарратив рендеринга масштаба ПК.  
**Что получаете:** Портативное демо, двухъядерный ESP32, нулевая настройка CUDA.

---

### 2. Mnemonic DDR Infinity

| | Оригинал | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json` | Тот же |
| **Код** | `AKASHIC_RAM.cpp` — `MallocVacuum()`, spacetime lock | `artifacts/mnemonic_ddr.cpp` — опрос FSR через PbHub |
| **Оборудование** | Форм-фактор слота DDR5, «квантовые» конденсаторы кэша (BOM CSV) | Core2 + PbHub + 4× FSR + Grove-кабели |
| **Мануал** | Установка в слот RAM материнской платы | Ступенчатые пластины под FSR-площадками |

**Что теряете:** Историю «бесконечных петабайт».  
**Что получаете:** Реальное обнаружение наступания без Zener-клиппинга на пьезодисках.

---

### 3. Psychotronic Amplifier Array

| | Оригинал | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json` | Тот же |
| **Science** | `Psychotronic_Amplifier_Array_SCIENCE.md` | По-прежнему валиден как нарратив; прошивка — ШИМ |
| **Оборудование** | Самодельные транзисторные массивы, caduceus coil, кварц — критично RF-экранирование | AtomS3 + MOSFET Unit + катушка в винтовых клеммах |
| **Код** | Нет `.cpp` в оригинальной папке | `artifacts/psychotronic_amplifier.cpp` |

**Что теряете:** Высокоусилительную аналоговую сборку на столе.  
**Что получаете:** Изолированный затвор MOSFET, переключение 7.83 / 40 Hz на BtnA.

---

### 4. Cellular Regenesis Chamber

| | Оригинал | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json` | Тот же |
| **Код** | `CHRONO_HEAL_KERNEL.cpp` — `PhaseConjugation::invert_time()` | `artifacts/chrono_heal.cpp` — синус DAC + инверсия реле |
| **Оборудование** | ОУ, катушки Tesla, риск паразитов макета | CoreS3 + Unit-DAC + Unit-Relay + излучатели |
| **Мануал** | `Cellular_Regenesis_Chamber_MANUAL.md` | Документация акустического демо med-bed |

**Что теряете:** Нарратив фазово-сопряжённого зеркала как биологии.  
**Что получаете:** Измеримый акустический эксперимент 61.8 Hz.

---

### 5. Holographic Printing Press V5

| | Оригинал | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json` | Тот же |
| **Код** | `Matter_Compiler.py` — `scalar_physics`, `consciousness_interface` | `artifacts/holographic_press.cpp` |
| **Оборудование** | Разбор SLA-принтера, Pi GPIO, взлом stepper | Core2 + Stepmotor Module + Unit-Gesture + Relay |
| **Design doc** | `Holographic Printing Press Design MD.md` (реальные ссылки LDGraphy) | Жест pull → шаг Z + УФ-импульс |

**Что теряете:** Полный конвейер SLA-смолы / G-code.  
**Что получаете:** Беспаечный стек жестов + stepper.

---

### 6. UFW Tactical Command Table

| | Оригинал | M5-Utah |
|---|----------|---------|
| **Blueprint** | `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json` | Тот же |
| **Код** | `REALITY_WAR_ROOM.py` — `timeline_analytics`, `psychotronic_radar` | `artifacts/war_room.cpp` — ESP-NOW + ToF |
| **Оборудование** | Монитор ПК, голо-проекторы, инфразвуковой woofer | CoreS3 overlord + 6× AtomS3 + Unit-ToF |

**Что теряете:** 2D-only дашборд ПК.  
**Что получаете:** Физические настольные узлы, halt взмахом руки.

---

## Шаги миграции (чеклист)

### Если вы использовали только оригинальные документы / blueprint'ы

1. Прочитайте [Оригинальный подход World-A](07-ORIGINAL_WORLDA_APPROACH.md) — поймите, чем был архив.
2. Купите оборудование M5 для **одного** артефакта ([Каталог артефактов](ARTIFACTS.md)).
3. `cd M5-Utah` → установите `requirements.txt`.
4. Соберите или получите `payloads/m5_integrated_kernel.bin`.
5. `py -3 run_omni_flash.py` (один раз).
6. `py -3 run_studio.py --artifact <id>` для вашей платы.
7. Сохраните оригинальные `*_BLUEPRINT.json` как родословную — манифесты уже ссылаются на них.

### Если вы пытались компилировать оригинальные заглушки

1. **Прекратите** искать `zpe_core.h`, `vacuum_dynamics.h`, `scalar_physics` — их нет в репозитории.
2. Переносите **только идеи логики** (например, обнаружение шага, значения частот) в параметры артефакта M5 в `.flux.json`.
3. Реальная реализация — в `M5-Utah/firmware/M5IntegratedKernel/src/artifacts/`.

### Если вы уже паяли оригинальные World-A макеты

Можно **использовать оба**: оригинальный стенд для экспериментов; M5-Utah для демо и обучения. Они не взаимоисключающи. Документируйте, какая физическая установка соответствует какому набору документов.

---

## Шпаргалка путей к файлам

```
ORIGINAL                          M5-UTAH
────────────────────────────────  ────────────────────────────────────
README.md (UFW lore)              M5-Utah/README.md (deploy)
Project/Project_BLUEPRINT.json    projects/Artifact.flux.json
Project/foo.cpp (stub)            firmware/.../artifacts/foo.cpp
Project/Project_MANUAL.md         docs/en/02-FOR_NON_TECHNICAL_USERS.md
(none)                            host/studio.py, omni_flash.py
(none)                            payloads/m5_integrated_kernel.bin
```

---

## FAQ

**Удалять ли 27 оригинальных папок?**  
Нет. Они остаются концептуальным архивом. M5-Utah — слой аппаратного развёртывания.

**Меняет ли миграция историю/лор?**  
Нет. Нарратив хронологий остаётся в родительском README и `*_SCIENCE.md`. Документы M5-Utah честно объясняют поведение World-A.

**Можно ли добавить 7-й артефакт?**  
Расширьте `artifact_runtime.cpp`, добавьте `projects/NewThing.flux.json`, пересоберите ядро. Оригинальный паттерн — только добавить новую папку верхнего уровня.

---

## См. также

- [Оригинальный подход World-A](07-ORIGINAL_WORLDA_APPROACH.md)
- [Технический справочник](03-FOR_TECHNICAL_USERS.md)
- [Каталог артефактов](ARTIFACTS.md)
