# CLAUDE.md

このファイルは、Claude Code (claude.ai/code) がこのリポジトリでコードを扱う際のガイダンスを提供します。

## プロジェクト概要

テクノバンド「空手バカボン」の日本語ファンサイトで、静的なGitHub Pagesサイトとして構築されています。2000年代前半の日本のWebデザインの美学を、HTMLテーブル、アニメーションGIF、レトロなスタイリングで再現しています。

## デプロイ

サイトは`master`ブランチからGitHub Pages経由でデプロイされます。純粋な静的HTML/CSS/JSのため、ビルドプロセスは不要です。

- **公開サイト**: https://karattebakabon.github.io/
- **ブランチ**: `master` (プッシュ時に自動デプロイ)
- **Jekyll**: `.nojekyll`ファイルで無効化

## アーキテクチャ

### ファイル構造
- `index.html` - バンドメニューとSNSウィジェットを含むメインホームページ
- `profile.html`, `susume.html`, `kotou.html`, `zunou.html` など - 各アルバム/コンテンツページ
- `rireki.html` - サイト更新履歴（ホームページにiframeで埋め込み）
- `collection/` - ライブ音源ページ
- `css/` - 手書きCSSファイル（style1.css～style4.css）
- `js/` - DragDealer.jsライブラリとはてなブックマーク連携
- `daycount/` - Perl CGIアクセスカウンターシステム
- `rss/` - RDF形式のRSSフィード
- `image/` - 画像、バナー、ファビコン
- `sound/` - MP3音声ファイル

### 主要技術
- **フロントエンド**: テーブルベースレイアウトの純粋なHTML4/HTML5
- **スタイリング**: レトロエフェクト付き手書きCSS（十字カーソル、スクロールバースタイリング）
- **JavaScript**: UI操作用DragDealer.js、SNSウィジェット
- **CGI**: アクセス計測用Perlスクリプト（daycount.cgiシステム）
- **解析**: Google Analytics（レガシーUA追跡）

### CSSアーキテクチャ
複数のCSSファイルがそれぞれ異なる目的を持ちます：
- `style1.css` - レトロカラースキーム（#102806 ダークグリーン背景）のメインスタイリング
- `style2.css`, `style3.css`, `style4.css` - 追加のスタイリングバリエーション
- `dragdealer-main.css` - DragDealer.jsコンポーネント用スタイリング

### CGIシステム
`daycount/`ディレクトリには完全なPerlベースのアクセスカウンターが含まれています：
- `daycount.cgi` - メインカウンタースクリプト
- `init.cgi` - 設定ファイル
- `check.cgi`, `conv.cgi` - ユーティリティスクリプト
- `gif1/`, `gif2/` - カウンター表示用数字画像

## コンテンツ管理

### RSSフィード
RSSフィードは`rss/rss.rdf`でRDF形式として手動で管理されています。更新時には以下を含める必要があります：
- 適切な日付形式の新しいエントリ
- セクションへのアンカーリンク（例：`#he20250623`）

### 更新履歴
サイトの変更は`rireki.html`に記録され、ホームページにiframeとして埋め込まれています。

## GitHub Actions

単一のワークフロー：`.github/workflows/file-update-notification.yml`
- masterへのプッシュ/PRで実行
- 通知目的で変更されたファイルをリスト表示
- 実際のビルドやデプロイステップなし

## 開発メモ

### スタイリング規則
- テーブルベースレイアウトの使用（意図的にレトロ）
- カラースキーム：ダークグリーン（#102806）背景、ライトグレー（#DDDDDD）テキスト、ブルー（#9999FF）リンク
- リンクに十字カーソル（`cursor: crosshair`）
- CSSで画像のドラッグ/右クリックを無効化
- スムーススクロール有効

### HTMLパターン
- `<font>`タグとインラインスタイリングを多用（時代に適合）
- cellpadding/cellspacingを使ったテーブルベースレイアウト
- 埋め込みSNSウィジェット（Twitter、Facebook、Feedly）
- iTunes Storeアフィリエイトリンク

### 音声統合
`sound/`ディレクトリのMP3ファイルは、各種ページでBGMや効果音として参照されています。

## 一般的なタスク

コンテンツ更新時：
1. 関連するHTMLファイルを直接修正
2. 変更履歴を`rireki.html`に更新
3. 新コンテンツ追加時は`rss/rss.rdf`を更新
4. masterへのプッシュでGitHub Pages経由で自動デプロイ

新ページ追加時：
1. 既存のHTML構造とCSSクラスに従う
2. 適切なmetaタグとGoogle Analyticsを含める
3. 関連する親ページからナビゲーションリンクを追加
4. 重要な更新にはRSSフィードエントリの追加を検討