
# プロジェクト: 非公式 空手バカボン WEBSITE

ユーザーには日本語で応答してください。ギャル語だと一層喜ばれます。

## 概要

このプロジェクトは、1980〜90年代に活動した日本のインディーズバンド「空手バカボン」の非公式ファンサイトです。
2003年から続く手書きのHTMLサイトを、GitHub Pagesを利用して公開しています。

サイトURL: https://karattebakabon.github.io/

## 主要技術

- **フロントエンド:**
  - HTML4 / HTML5 (手書き)
  - CSS (手書き)
  - JavaScript
    - [DragDealer.js](https://skidding.github.io/dragdealer/): UIコンポーネント
- **バックエンド:**
  - Perl: アクセスカウンタCGIとして利用 (`daycount/` ディレクトリ)
- **ホスティング:**
  - GitHub Pages
- **その他:**
  - Google Analytics (UA)
  - Woopra
  - RSS (`rss/rss.rdf`)
  - OGP

## コーディング規約・特徴

- **レトロなWebデザイン:** 2000年代初頭の個人サイトの雰囲気を色濃く残したデザインが特徴です。`<marquee>` タグや `crosshair` カーソルなど、当時を彷彿とさせる要素が意図的に使用されています。
- **手書きコード:** フレームワークや静的サイトジェネレータは使用せず、HTMLとCSSは基本的に手書きで作成されています。
- **ファイル名:** `susume.html` (ススメ)、`kotou.html` (孤島) のように、日本語をローマ字にしたファイル名が多く、全体的にカオスな状態です。これはプロジェクトの歴史的な経緯によるものです。
- **文字コード:** 主に `UTF-8` が使用されています。

## ディレクトリ構造

`README.md` に記載されている主要なディレクトリ構造は以下の通りです。

```
├── index.html          # トップページ
├── profile.html        # バンド概要
├── susume.html         # 作品ページ（ソノシート/EP）
├── kotou.html          # 作品ページ（孤島の檻）
├── zunou.html          # 作品ページ（頭脳改革）
├── collection/         # CD『ナゴムコレクション』ライブ音源
├── css/                # 手書き + DragDealer 用スタイル
├── js/                 # DragDealer & はてブ読込スクリプト
├── daycount/           # アクセスカウンタ CGI 一式
├── rss/                # RSS フィード
├── .github/workflows/  # ファイル変更を Slack に投げるだけの CI
└── .well-known/        # Brave Rewards / Nostr 検証ファイル
```

## 開発・デプロイ

- `main` ブランチがGitHub Pagesに直接デプロイされます。
- `.github/workflows/file-update-notification.yml` により、ファイルの更新時にSlack通知が実行されます。

## Gemini CLIによる変更履歴

このプロジェクトでは、Gemini CLIを導入し、以下の作業を行いました。

- `rireki.html` にGemini CLIの導入に関する更新履歴エントリを追加しました。
- `rss/rss.rdf` にも同様の更新履歴エントリを追加し、日付を更新しました。
- これらの変更はGitにコミットされ、GitHubリポジトリにプッシュされました。
