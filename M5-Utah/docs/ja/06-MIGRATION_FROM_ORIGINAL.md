# 移行ガイド: オリジナル UFW → M5-Utah

このガイドは、**オリジナルアーカイブレイアウト**（27プロジェクトフォルダ、スタブ、マニュアル）から始めて、**M5-Utah**（M5Stack + Flux デプロイメント）に移行する人向けです。

---

## 概要

| トピック | オリジナル（M5以前） | M5-Utah |
|-------|-------------------|---------|
| **コードの場所** | `ProjectName/Reality_Engine.cpp`、`Matter_Compiler.py` など | `M5-Utah/firmware/.../artifacts/*.cpp` + `projects/*.flux.json` |
| **ハードウェア** | カスタムブレッドボード、はんだ付け、Arduino、Pi、CUDA PC | M5Stack Grove モジュール、はんだ付け不要 |
| **ビルド** | ビルド不可（架空の `#include`） | PlatformIO + `build_kernel.ps1` |
| **デプロイ** | 概念的マニュアルのみ | 一度 `omni_flash.py`、その後 `studio.py` |
| **デバイスタイプの切り替え** | プロジェクトごとに再配線／再コンパイル | 新しい `.flux.json` マニフェストを選択 |
| **依存関係** | `zpe_core.h`、`scalar_physics` など（欠落） | M5Unified、ArduinoJson、pyserial |

---

## アーティファクト別移行マップ

### 1. Zero Point GPU Emulator

| | オリジナル | M5-Utah |
|---|----------|---------|
| **Blueprint** | `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json` | マニフェストで同じファイルを参照 |
| **Code** | `Reality_Engine.cpp` — `#include <zpe_core.h>`、CUDA クラス PC GPU | `artifacts/zero_point_gpu.cpp` — 2D 波計算 + LCD |
| **Hardware** | ホスト CPU + "Casimir Compute Gate" + HDMI | M5Stack CoreS3 + オプション DINBase |
| **Manual** | `The_Zero_Point_GPU_Emulator_MANUAL.md` — NVIDIA CUDA、16 GB RAM | [非技術者向け](02-FOR_NON_TECHNICAL_USERS.md) |

**移行で失うもの:** PC スケールのレンダリング物語。  
**移行で得るもの:** ポータブルデモ、デュアルコア ESP32、CUDA セットアップ不要。

---

### 2. Mnemonic DDR Infinity

| | オリジナル | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json` | 同じ |
| **Code** | `AKASHIC_RAM.cpp` — `MallocVacuum()`、時空間ロック | `artifacts/mnemonic_ddr.cpp` — PbHub FSR ポーリング |
| **Hardware** | DDR5 スロット形状、量子キャッシュコンデンサ（BOM CSV） | Core2 + PbHub + 4× FSR + Groveケーブル |
| **Manual** | マザーボード RAM スロット設置 | FSR パッド下のステッププレート |

**移行で失うもの:** 「無限ペタバイト」の物語。  
**移行で得るもの:** 圧電ディスクのツェナークリッピングなしの実際の踏み検出。

---

### 3. Psychotronic Amplifier Array

| | オリジナル | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json` | 同じ |
| **Science** | `Psychotronic_Amplifier_Array_SCIENCE.md` | 物語として依然有効; ファームウェアは PWM |
| **Hardware** | カスタムトランジスタアレイ、カドゥケウスコイル、石英 — RF シールドが重要 | AtomS3 + MOSFET Unit + ネジ端子のコイル |
| **Code** | オリジナルフォルダに `.cpp` なし | `artifacts/psychotronic_amplifier.cpp` |

**移行で失うもの:** 高ゲインアナログベンチビルド。  
**移行で得るもの:** 分離された MOSFET ゲート、BtnA で 7.83 / 40 Hz 切り替え。

---

### 4. Cellular Regenesis Chamber

| | オリジナル | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json` | 同じ |
| **Code** | `CHRONO_HEAL_KERNEL.cpp` — `PhaseConjugation::invert_time()` | `artifacts/chrono_heal.cpp` — DAC 正弦波 + リレー反転 |
| **Hardware** | オペアンプ、テスラコイル、ブレッドボード寄生リスク | CoreS3 + Unit-DAC + Unit-Relay + トランスデューサー |
| **Manual** | `Cellular_Regenesis_Chamber_MANUAL.md` | メッドベッド音響デモドキュメント |

**移行で失うもの:** 生物学としての位相共役ミラー物語。  
**移行で得るもの:** 測定可能な 61.8 Hz 音響実験。

---

### 5. Holographic Printing Press V5

| | オリジナル | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json` | 同じ |
| **Code** | `Matter_Compiler.py` — `scalar_physics`、`consciousness_interface` | `artifacts/holographic_press.cpp` |
| **Hardware** | SLA プリンター分解、Pi GPIO、ステッパーハッキング | Core2 + Stepmotor Module + Unit-Gesture + Relay |
| **Design doc** | `Holographic Printing Press Design MD.md`（実在の LDGraphy 参照） | ジェスチャープル → Z ステップ + UV パルス |

**移行で失うもの:** 完全なレジン SLA パイプライン / G-code。  
**移行で得るもの:** はんだレスジェスチャー + ステッパースタック。

---

### 6. UFW Tactical Command Table

| | オリジナル | M5-Utah |
|---|----------|---------|
| **Blueprint** | `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json` | 同じ |
| **Code** | `REALITY_WAR_ROOM.py` — `timeline_analytics`、`psychotronic_radar` | `artifacts/war_room.cpp` — ESP-NOW + ToF |
| **Hardware** | PC モニター、ホロプロジェクター、超低周波音ウーファー | CoreS3 オーバーロード + 6× AtomS3 + Unit-ToF |

**移行で失うもの:** 2D のみの PC ダッシュボード。  
**移行で得るもの:** 物理デスクノード、手振り停止。

---

## 移行手順（チェックリスト）

### オリジナルドキュメント／ブループリントのみ使用していた場合

1. [オリジナル World-A アプローチ](07-ORIGINAL_WORLDA_APPROACH.md) を読む — アーカイブが何だったかを理解する。
2. **1つ**のアーティファクト用 M5 ハードウェアを購入（[アーティファクトカタログ](ARTIFACTS.md)）。
3. `cd M5-Utah` → `requirements.txt` をインストール。
4. `payloads/m5_integrated_kernel.bin` をビルドまたは入手。
5. `py -3 run_omni_flash.py`（一度）。
6. ボードに合った `py -3 run_studio.py --artifact <id>`。
7. オリジナル `*_BLUEPRINT.json` を系譜として保持 — マニフェストは既にリンク済み。

### オリジナルスタブのコンパイルを試みていた場合

1. `zpe_core.h`、`vacuum_dynamics.h`、`scalar_physics` の追跡を**やめる** — リポジトリに存在しない。
2. **ロジックのアイデアのみ**を移植（例: ステップ検出、周波数値）を `.flux.json` の M5 アーティファクトパラメータに。
3. 実装は `M5-Utah/firmware/M5IntegratedKernel/src/artifacts/` にある。

### オリジナル World-A ブレッドボードを既にはんだ付け済みの場合

**両方実行可能**: 実験用のオリジナルベンチリグ; デモと教育用の M5-Utah。相互排他的ではない。どの物理セットアップがどのドキュメントセットに対応するか文書化する。

---

## ファイルパス早見表

```
ORIGINAL                          M5-UTAH
────────────────────────────────  ────────────────────────────────────
README.md (UFW lore)              M5-Utah/README.md (deploy)
Project/Project_BLUEPRINT.json    projects/Artifact.flux.json
Project/foo.cpp (stub)            firmware/.../artifacts/foo.cpp
Project/Project_MANUAL.md         docs/ja/02-FOR_NON_TECHNICAL_USERS.md
(none)                            host/studio.py, omni_flash.py
(none)                            payloads/m5_integrated_kernel.bin
```

---

## FAQ

**27のオリジナルフォルダを削除するか？**  
いいえ。概念的アーカイブとして残ります。M5-Utah はハードウェアデプロイメントレイヤーです。

**移行は物語／ロアを変えるか？**  
いいえ。タイムライン物語は親 README と `*_SCIENCE.md` に残ります。M5-Utah ドキュメントは World-A 動作を正直に説明します。

**7つ目のアーティファクトを追加できるか？**  
`artifact_runtime.cpp` を拡張し、`projects/NewThing.flux.json` を追加し、カーネルを再ビルド。オリジナルパターンは新しいトップレベルフォルダの追加のみでした。

---

## 関連項目

- [オリジナル World-A アプローチ](07-ORIGINAL_WORLDA_APPROACH.md)
- [技術リファレンス](03-FOR_TECHNICAL_USERS.md)
- [アーティファクトカタログ](ARTIFACTS.md)
