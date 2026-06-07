# 用語集

M5-Utah と広い UFW アーカイブで使われる用語の平易な定義。

| 用語 | 意味 |
|------|---------|
| **Artifact（アーティファクト）** | デバイスモード — 例: ステップパッドコントローラー、波ディスプレイ、ジェスチャープリンター。`studio.py` で1つ選ぶ。 |
| **Blueprint（ブループリント）** | 親リポジトリ内のアーティファクトの概念的コンポーネントを記述する JSON ファイル（`*_BLUEPRINT.json`）。 |
| **ESP32** | M5Stack デバイス内部のマイクロコントローラー。カーネルファームウェアを実行する。 |
| **Flux manifest（Flux マニフェスト）** | デバイスにどのアーティファクトをどの設定で実行するかを伝える `.flux.json` ファイル。 |
| **FSR** | Force Sensitive Resistor — 踏むと感知するパッド。 |
| **Grove cable（Groveケーブル）** | M5Stack ユニットで使われる色分けプラグケーブル（はんだ付け不要）。 |
| **I2C** | アドオンモジュール（PbHub、DAC、センサー）と通信する2線式バス。 |
| **JIT injection（JIT インジェクション）** | USB 経由でマニフェストを送信し、再フラッシュなしでデバイスモードを切り替えること。 |
| **Kernel / Lazarus Kernel（カーネル）** | `M5IntegratedKernel` — 一度フラッシュするベースファームウェア; その後マニフェストを受信する。 |
| **Manifest（マニフェスト）** | Flux マニフェストと同じ。 |
| **M5Stack** | モジュラー ESP32 ガジェットのブランド（画面、センサー、積み重ね可能なユニット）。 |
| **Omni-Flash** | `omni_flash.py` — 空の M5Stack にカーネルをフラッシュするツール。 |
| **PbHub** | I2C 経由で最大6つのアナログセンサーを読み取る M5Stack ユニット。 |
| **PSRAM** | 一部の ESP32 ボードにある追加 RAM。大きなバッファに使用。 |
| **Sovereign Node（ソブリン・ノード）** | プロジェクト内で Lazarus Kernel を実行する M5Stack の呼び名。 |
| **Studio / Utah Flux Host** | `studio.py` — マニフェストを一覧表示しインジェクトするツール。 |
| **UFW** | Utah Future Weapons — このリポジトリのプロジェクトファミリー名。 |
| **World-A** | リポジトリ内の用語。現代の物理的に構築可能なデプロイメント（タイムラインの物語に対して）。 |
| **Zero-click（ゼロクリック）** | エンドユーザーが Arduino IDE を開いたりコードをコンパイルしたりしないこと。 |

## ロア用語（物語 — エンジニアリング仕様ではない）

これらはブループリントとストーリーテキストに登場します。**プロジェクト語彙**であり、検証済みの物理学ではありません:

- Akashic Record / Cloud（アカシックレコード／クラウド）
- Phase-conjugate / Priore Effect（メッドベッドの主張として）
- Psychotronic / scalar waves（サイコトロニック／スカラー波）
- Zero Point Energy (ZPE) as infinite power source（零点エネルギーを無限電源として）
- Vacuum memory / spacetime locking（真空メモリー／時空間ロック）

これらが実際のハードウェア動作にどう対応するかは [科学者向け](04-FOR_SCIENTISTS.md) と [懐疑派向け](05-FOR_SKEPTICS.md) を参照。
