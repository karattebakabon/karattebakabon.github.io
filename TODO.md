# TODO — 空手チョップをもう一度。改善リスト

2026-09-01 作成。サイト実地調査（外部サービス生死確認込み）に基づく。
優先度: **P0=死んでるものを直す** / **P1=モダン化・SEO** / **P2=やっておくと良い**。

旧TODO（2019年 TaskPaper 形式）の未了5項目は、更新履歴（2019-12-01/12-28の項）と突合の結果すべて実施済みと確認 → `archive/TODO_2019` へ退避済み。

---

## P0: 死亡中の外部パーツ（要メンテ）

- [x] **Pocket 保存ボタンを削除** — `index.html`。getpocket.com の btn.js が 503 を返す（Pocket は 2025年にサービス終了）。`pocket-btn` アンカー＋スクリプトをまるごと削除。✅ 2026-09-01
- [x] **ezcounter アクセスカウンターを CF Worker に置換** — `index.html`。死亡した ezcounter テーブルを撤去し、自前 Worker `karatte-counter`（`counter-worker/`・KV保存・JST日替わり・today/yesterday/total SVG表示）の img タグに差し替え。✅ 2026-09-06 デプロイ済み（https://karatte-counter.emerald-pencil.workers.dev）
- [x] **Tweet ボタンを復活** — `index.html`。読み込みスクリプトが欠けていたため `https://platform.twitter.com/widgets.js`（200 生存確認済み）を defer で追加。✅ 2026-09-01
- [x] **iTunes バッジを `music.apple.com` 直リンクに統一** — `index.html`/`kotou.html`/`susume.html`/`zunou.html`。linkmaker のバッジ画像は取得不能＋アフィリエイト ID（`at=10l78s`）無効のため、『♪Apple Musicで聴く』テキストリンク（`music.apple.com`・301 生存確認済み）に置換。併せて説明文の「iTunes」「価格1200円」表記も更新。✅ 2026-09-01

## P1: モダン化・SEO

- [x] **CF Worker アクセスカウンター（完成）** — P0 の ezcounter 項目で完了済み。✅ 2026-09-06
- [x] **OGP / Twitter Card を追加** — 全18ページに og:site_name / og:type / og:url / og:title / og:image / og:description（description保持ページのみ）＋ `twitter:card=summary` を挿入。✅ 2026-09-06
- [x] **sitemap.xml に `<lastmod>` を追加** — 51URLすべてに git 最終コミット日ベースの lastmod を付与（XMLパース検証済み）。✅ 2026-09-06
- [x] **RSS の重複項目を解消（A案）** — `rss/rss.rdf` の全 item `rdf:about`・`rdf:li` を `rireki.html#heXXXXMMDD` 実アンカーへ統一。`rireki.html` 側に15個の `<a id>` を付与し、5月14日の2件は `he20260514` / `he20260514b` で分離（about 15/15・li 14/14 全ユニーク・XMLパース検証済み）。✅ 2026-09-06
- [x] **GA 関連の掃除** — `// UA-366570-5` コメント21ファイル分削除、廃止済み `verify-v1` メタタグ削除。✅ 2026-09-06
- [x] **rireki.html の GA 二重計上を止める** — iframe 内の gtag スニペットを削除。✅ 2026-09-06
- [x] **404.html を作る** — レトロ調「404 — 空手チョップはずれた。」ページを新規作成。✅ 2026-09-06
- [x] **残存 http:// リンクの https 化** — collection / index / link / rireki / yamaarashi / zunou の28リンクを https 化（rireki_old 系は原文保持のため対象外）。✅ 2026-09-06

## P2: 整理・容量・遊び

- [x] **css.txt の正規取り込み → 削除** — `.rirekiWraper`/`.iframeWrap`（＋iframe絶対配置）定義を `css/style1.css` 末尾へ取り込み、css.txt 本体は git rm（末尾の死亡 neoearth iframe も同時に消滅）。✅ 2026-09-06
- [x] **.gitignore 追加** — `log/`、`2026-*.txt` を追加。✅ 2026-09-06
- [x] **daycount/（Perl CGI）を削除** — 実参照ゼロ（rireki_old3 の言及のみ）・データも 2015年で凍結（total 15）と確認の上で完全削除。コミット履歴でいつでも復元可能。✅ 2026-09-06
- [x] **更新履歴の棚卸し** — 2018〜2025年分を `rireki_old4.html`（282行）へ分離。rireki.html は151行に短縮。old1〜3 準拠のフッタリンク（「YYYY年までの更新履歴→こちら」形式）＋sitemap.xml への追加＋RDF の移動エントリ7件を rireki_old4.html アンカーへ書き換え（RDF↔アンカー整合 15/15 検証済み）。✅ 2026-09-06

---

## やらないこと（判断済み）

- **Cloudflare CDN 前段化／独自ドメイン化** — github.io は元々 Fastly CDN で配信されており速度改善の余地がなく、独自ドメイン購入も見送り（2026-09-01 決定）。CF アカウントは API プロキシとアクセスカウンター専用。
- **デザインのモダン刷新** — テーブルレイアウト・crosshair カーソル・marquee は「2000年代前半の美学」として意図的に保持。
- **GA4 Data API による カウンター再現** — 14ヶ月制限・メンテ負担の問題から不採用（2026-09-01 決定）。CF Worker 案に統合。
- **sound/（26MB）の軽量化** — 手出し無用として永久保留（2026-09-06 指示）。ビットレート再エンコード等は実施しない。

## 作業メモ

- P0 作業で `index.html`/`kotou.html`/`susume.html`/`zunou.html` を編集した際、行末が CRLF→LF に変わった（`core.autocrlf=true` 環境のため実質差分は少ない。コミット時は `--ignore-cr-at-eol` で確認推奨）。
- `session-ses_1bae.md` はルートから `log/` へ移動済み（git では削除＋未追跡の状態）。次回コミット時に反映。
- CLAUDE.md / GEMINI.md / 旧TODO は `archive/` へ移動済み（git mv 済み・履歴保持）。
