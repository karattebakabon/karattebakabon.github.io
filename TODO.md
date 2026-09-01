# TODO — 空手チョップをもう一度。改善リスト

2026-09-01 作成。サイト実地調査（外部サービス生死確認込み）に基づく。
優先度: **P0=死んでるものを直す** / **P1=モダン化・SEO** / **P2=やっておくと良い**。

旧TODO（2019年 TaskPaper 形式）の未了5項目は、更新履歴（2019-12-01/12-28の項）と突合の結果すべて実施済みと確認 → `archive/TODO_2019` へ退避済み。

---

## P0: 死亡中の外部パーツ（要メンテ）

- [ ] **Pocket 保存ボタンを削除** — `index.html`。getpocket.com の btn.js が 503 を返す（Pocket は 2025年にサービス終了）。`pocket-btn` アンカー＋スクリプトをまるごと削除。
- [ ] **ezcounter アクセスカウンターを撤去** — `index.html`。カウンター画像 URL が応答せず数字が表示されない。カウンターテーブル＋`(2015年11月13日カウンターリセット)` の扱いを決める（削除 or GA ベースの代替表示）。
- [ ] **Tweet ボタンを復活か削除** — `index.html`。`twitter.com/share` のアンカーはあるが読み込みスクリプト（widgets.js）が存在せず何も描画されない。`https://publish.x.com/widgets.js` に差し替えるか、タグごと削除。
- [ ] **iTunes バッジの張り直し** — `index.html` ほか4ファイル。linkmaker.itunes.apple.com のバッジ画像が取得不能＋アフィリエイト ID（`at=10l78s`）は LinkShare 廃止で無効の可能性大。バッジ img を外してテキストリンク化、または `music.apple.com` 直リンク（301 で生存確認済み）に統一。

## P1: モダン化・SEO

- [ ] **OGP / Twitter Card を追加** — 全ページ og:title / og:description / og:image（`image/Untitled1.jpg` か banner.gif）/ `twitter:card`。現在ゼロで、SNS シェア時にカードが出ない。
- [ ] **sitemap.xml に `<lastmod>` を追加** — 現在 loc/changefreq/priority のみで更新日が無い。
- [ ] **RSS の重複項目を解消** — `rss/rss.rdf` に同一 `rdf:about`（`#he20260514`）の item が2件。
- [ ] **GA 関連の掃除** — 全21ファイルで GA4（G-D90CGM907G）に統一済み。残作業: `// UA-366570-5` コメント削除、廃止済みの `verify-v1` メタタグ削除。
- [ ] **rireki.html の GA 二重計上を止める** — 更新履歴 iframe 内でも gtag が動いていて、トップページ表示時にページビューが二重に計上される。iframe 側の gtag を外す。
- [ ] **404.html を作る** — 現在不存在。GitHub Pages は 404.html を自動採用するので、レトロ調の「空手チョップもどってきて！」ページを用意。
- [ ] **残存 http:// リンクの https 化** — collection / index / link / yamaarashi / zunou / rireki 系（mixi・bookmeter・hateblo・lastfm 等）。今のところ実害はないが、外部サービスの前途は https 化に合わせて確認。

## P2: 整理・容量・遊び

- [ ] **css.txt の正規取り込み or 削除** — ルートの css.txt には `rirekiWraper` / `iframeWrap` の定義が入っているが、どこにも読み込まれていない（＝このクラスは現在無効）。style1.css へ取り込むか削除する。
- [ ] **.gitignore 追加** — `log/`、`2026-*.txt`（ルートの作業ログ類）。
- [ ] **daycount/（Perl CGI）の取り扱い決定** — GitHub Pages では動かない死蔵品。rireki_old3 からのみ言及あり。archive/ へ退避するか現状維持か決める。
- [ ] **sound/ の軽量化検討** — 26MB。`yamaarashi/yamaarashi.html` からのみ参照。ビットレート見直しや m4a/opus 化で帯域節約（レトロ感を損なわない範囲で）。
- [ ] **更新履歴の浅い部分の棚卸し** — rireki.html が 369 行で伸び続けている。過去分は rireki_old 系への追い出しの検討。

---

## やらないこと（判断済み）

- **Cloudflare CDN 前段化／独自ドメイン化** — github.io は元々 Fastly CDN で配信されており速度改善の余地がなく、独自ドメイン購入も見送り（2026-09-01 決定）。CF アカウントは API プロキシ専用。
- **デザインのモダン刷新** — テーブルレイアウト・crosshair カーソル・marquee は「2000年代前半の美学」として意図的に保持。
- **PHP/SSG への移行** — 静的 HTML 手書き運用は継続（AI ツールでの編集体制が確立済み）。

## 作業メモ

- `session-ses_1bae.md` はルートから `log/` へ移動済み（git では削除＋未追跡の状態）。次回コミット時に反映。
- CLAUDE.md / GEMINI.md / 旧TODO は `archive/` へ移動済み（git mv 済み・履歴保持）。
