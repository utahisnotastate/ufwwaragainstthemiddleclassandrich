# アーティファクトカタログ

6つの UFW アーティファクトが M5-Utah 経由で今日デプロイ可能です。各行には**購入するもの**、**World-A でデバイスが実際に行うこと**、**オリジナルブループリントの場所**を記載しています。

## 概要表

| # | 名前 | M5 ボード | アドオン | World-A の動作 |
|---|------|----------|---------|------------------|
| 1 | Zero Point GPU Emulator | CoreS3 | DINBase（冷却オプション） | 画面にアニメーション波グリッド; 1つの CPU コアで計算、もう1つで描画 |
| 2 | Mnemonic DDR Infinity | Core2 | PbHub + 4× FSR + Groveケーブル | ステップパッドが「メモリー書き込み」イベントをトリガー; 画面にカウント表示 |
| 3 | Psychotronic Amplifier Array | AtomS3 | MOSFET Unit + 手巻きコイル | 7.83 Hz または 40 Hz の PWM オシレーター; 外部 PSU がコイルを駆動 |
| 4 | Cellular Regenesis Chamber | CoreS3 | Unit-DAC + Unit-Relay + トランスデューサー | DAC で 61.8 Hz 正弦波; 音響実験用にリレーで位相反転 |
| 5 | Holographic Printing Press V5 | Core2 | Stepmotor + Unit-Gesture + Unit-Relay | 手のスワイプ検出 → Z ステップカウンター + UV リレーパルス（デモ） |
| 6 | UFW Tactical Command Table | CoreS3 | Unit-ToF + 6× AtomS3 Lite（スワーム） | ESP-NOW ブロードキャスト; ToF 手振りで停止／実行を切り替え（オーバーロードノード） |

## アーティファクト別詳細

### 1. Zero Point GPU Emulator

- **Manifest:** `projects/Zero_Point_GPU.flux.json`
- **Blueprint:** `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json`
- **Source stub:** `The_Zero_Point_GPU_Emulator/Reality_Engine.cpp`
- **Assembly:** CoreS3 を DINBase にスナップ; USB-C で PC に接続。
- **Verify:** 画面にライブカラーグリッドが表示; シリアルにフレーム更新を出力。

### 2. Mnemonic DDR Infinity (Step Machine)

- **Manifest:** `projects/Mnemonic_DDR_Infinity.flux.json`
- **Blueprint:** `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json`
- **Source stub:** `Mnemonic_DDR_Infinity/AKASHIC_RAM.cpp`
- **Assembly:** PbHub を Port A に; FSR ユニットを CH0–CH3 に; ステッププレートの下に取り付け。
- **Verify:** パッドを踏む → シリアルに `[DDR] Memory write` をログ; 画面のカウンターが増加。

### 3. Psychotronic Amplifier Array (PAA)

- **Manifest:** `projects/Psychotronic_Amplifier_Array.flux.json`
- **Blueprint:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json`
- **Science doc:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_SCIENCE.md`
- **Assembly:** MOSFET を Port A に; コイルリードをネジ端子に; **コイル電流には外部 PSU を使用**。
- **Verify:** MOSFET 出力のオシロスコープで約 7.83 Hz または 40 Hz の矩形波; AtomS3 の BtnA を押してモード切り替え。

### 4. Cellular Regenesis Chamber (Med-Bed)

- **Manifest:** `projects/Cellular_Regenesis_Chamber.flux.json`
- **Blueprint:** `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json`
- **Source stub:** `Cellular_Regenesis_Chamber/CHRONO_HEAL_KERNEL.cpp`
- **Assembly:** Unit-DAC を Port A に; Unit-Relay を Port B に; オーディオトランスデューサーを端子ブロックに。
- **Verify:** DAC が正弦波を出力; リレーが半周期反転でトグル; シリアルに `[CHRONO]` をログ。

### 5. Holographic Printing Press V5

- **Manifest:** `projects/Holographic_Printing_Press_V5.flux.json`
- **Blueprint:** `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json`
- **Source stub:** `Holographic_Printing_Press_V5/Matter_Compiler.py`
- **Assembly:** Stepmotor を Core2 の下に積み重ね; Gesture を A に; Relay を B に; NEMA-17 をステッパー端子に。
- **Verify:** ジェスチャーセンサーで下スワイプすると Z が増加しリレーがパルス（UV デモ）。

### 6. UFW Tactical Command Table

- **Manifest:** `projects/UFW_Tactical_Command_Table.flux.json`
- **Blueprint:** `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json`
- **Source stub:** `UFW_Tactical_Command_Table/REALITY_WAR_ROOM.py`
- **Assembly:** CoreS3 を中央に; Unit-ToF を Port A に; ESP-NOW スワーム用にオプションで 6× AtomS3 Lite ワーカー。
- **Verify:** ToF 範囲内に手があると画面が HALT/ACTIVE を切り替え; シリアルモニターに ESP-NOW パケット。

## インジェクトコマンド

```bash
py -3 run_studio.py --artifact zero_point_gpu
py -3 run_studio.py --artifact mnemonic_ddr_infinity
py -3 run_studio.py --artifact psychotronic_amplifier_array
py -3 run_studio.py --artifact cellular_regenesis_chamber
py -3 run_studio.py --artifact holographic_printing_press_v5
py -3 run_studio.py --artifact ufw_tactical_command_table
```
