# オリジナル World-A アプローチ（M5Stack 以前）

**M5-Utah** 以前、UFW リポジトリは**27プロジェクトのフラットアーカイブ**として構成されていました。このドキュメントはそのオリジナルレイアウトを記述し、M5 移行パスと比較できるようにします。

---

## リポジトリ構造（オリジナル）

```
ufwwaragainstthemiddleclassandrich/
├── README.md
├── The_Zero_Point_GPU_Emulator/
│   ├── The_Zero_Point_GPU_Emulator_BLUEPRINT.json
│   ├── The_Zero_Point_GPU_Emulator_MANUAL.md
│   ├── The_Zero_Point_GPU_Emulator_SCIENCE.md
│   ├── Reality_Engine.cpp          ← スタブ、コンパイル不可
│   └── The_Zero_Point_GPU_Emulator_LANDING.html
├── Mnemonic_DDR_Infinity/
│   ├── Mnemonic_DDR_Infinity_BLUEPRINT.json
│   ├── Mnemonic_DDR_Infinity_BOM.csv
│   ├── AKASHIC_RAM.cpp
│   └── ...
├── ... (同じパターンの25プロジェクト)
└── (M5-Utah/ なし、ビルドシステムなし)
```

各プロジェクトには通常以下が含まれていました:

| ファイルタイプ | 目的 |
|-----------|---------|
| `*_BLUEPRINT.json` | コンポーネントグラフ / ジオメトリツリー |
| `*_SCIENCE.md` | 検証物語、方程式、mermaid |
| `*_MANUAL.md` | インストールと操作手順 |
| `*_3D.json` | シーンメタデータ |
| `*_LANDING.html` | 静的プロモページ |
| `*.cpp` / `*.py` | **架空のインポート**を含む概念的コード |

`requirements.txt`、PlatformIO、統一フラッシュツールは**ありませんでした**。

---

## ビルド方法（オリジナル仕様）

Batch 1–2 設計ブリーフ（M5 移行前）は**手作り World-A** リグを記述していました:

### Zero Point GPU
- **ソフトウェアパス:** **CUDA クラス PC** 上の真空/GPU ライブラリに対して `Reality_Engine.cpp` をコンパイル。
- **マニュアルの記載:** NVIDIA GPU、16 GB RAM、GCC、CUDA Toolkit。
- **現実:** `zpe_core.h` はリポジトリに存在しない。

### Mnemonic DDR Infinity
- **ハードウェアパス:** DDR5 スティック形状 **または** **Arduino** 上の圧電踏みディスク。
- **問題:** カスタム電圧クリッピング（ツェナー、プルダウン）、ブレッドボードノイズ。
- **BOM CSV:** 実在部品（Kingston DDR、Murata コンデンサ）と架空の「量子キャッシュ」が混在。

### Psychotronic Amplifier Array
- **ハードウェアパス:** 手はんだ付け高ゲイントランジスタ、カドゥケウスコイル、石英共振器。
- **問題:** 慎重なシールドなしの RF ノイズ（「光子クエンチング」）。
- **ドキュメント:** `Psychotronic_Amplifier_Array_SCIENCE.md`（信頼度 0.94）— 物語であり、ファームウェアではない。

### Cellular Regenesis Chamber
- **ハードウェアパス:** 露出オペアンプ、カスタムテスラコイル、ブレッドボード上の位相共役ミラー。
- **コード:** `CHRONO_HEAL_KERNEL.cpp` → `#include <phase_conjugation.h>`（欠落）。
- **その他:** `Telomere_Restore.cpp`、OpenSCAD ポッドジオメトリ。

### Holographic Printing Press V5
- **ハードウェアパス:** **Raspberry Pi GPIO** 経由で **SLA 3D プリンター** モータードライバーをリバースエンジニアリング。
- **ソフトウェア:** `Matter_Compiler.py` → `scalar_physics`、`consciousness_interface`（欠落）。
- **実在のエンジニアリング:** `Holographic Printing Press Design MD.md` は LDGraphy スタイルの設計を参照。

### UFW Tactical Command Table
- **ハードウェアパス:** PC モニター「God-Eye」ダッシュボード。
- **ソフトウェア:** `REALITY_WAR_ROOM.py` → `timeline_analytics`、`psychotronic_radar`（欠落）。
- **制限:** 2D 画面のみ; 物理スワームノードなし。

---

## オリジナルワークフロー（典型的なユーザー）

1. リポジトリをクローンし、プロジェクトフォルダを開く。
2. `*_MANUAL.md` と `*_BLUEPRINT.json` を読む。
3. `*.cpp` のコンパイルまたは `*.py` の実行を試みる → 欠落モジュールで**失敗**。
4. オプションで BOM / サイエンスドキュメントから**着想を得た**ブレッドボードを構築。
5. UFW 経済／タイムライン物語のためにルート `README.md` を読む。

**検証の物語:** ルート README の「使用可能なコード」は**概念的に使用可能なブループリント**を指し、単一の動作バイナリではなかった。

---

## オリジナル vs M5-Utah（概要）

| 次元 | オリジナル World-A | M5-Utah |
|-----------|------------------|---------|
| **組み立て** | はんだ、配線、電圧クリップ | Groveケーブル、ネジ端子 |
| **ツールチェーン** | Arduino IDE、プロジェクトごとの PlatformIO、CUDA、Pi | 1つのカーネル + マニフェストインジェクション |
| **コードステータス** | スタブ + ロア | コンパイル可能ファームウェア + Python ホスト |
| **プロジェクト数** | 27アーカイブ | 6デプロイ済みアーティファクト（追加予定） |
| **ユーザースキル** | 電気工学 + ソフトウェア | USB を接続しリストを選択 |
| **ブループリントの役割** | 主要仕様 | `.flux.json` 内のリンク系譜 |
| **正直なデモ** | 自己解釈が必要 | 科学者／懐疑派ガイドに文書化 |

---

## 今日オリジナルドキュメントを使う場合

| オリジナルを使う | M5-Utah を使う |
|--------------|-------------|
| ロア、SF、引用 | 実際にハードウェアをフラッシュ |
| OpenSCAD / 3D ジオメトリ | デスク上のステップパッド、波、ジェスチャー |
| 全27プロジェクトカタログ | 6つの MVP アーティファクト |
| **物語**に関する論文執筆 | 計測**プロトコル** |

---

## 前進するための移行

オリジナルフォルダから M5-Utah マニフェストへの段階的変換については **[移行ガイド](06-MIGRATION_FROM_ORIGINAL.md)** を参照。

---

## 関連項目

- [ドキュメントハブ](README.md)
- [アーティファクトカタログ](ARTIFACTS.md) — ブループリントパスと並列の M5 BOM
- 親リポジトリ `README.md` — 変更なしの UFW ミッションステートメント
