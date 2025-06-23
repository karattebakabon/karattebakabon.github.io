[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/karattebakabon/karattebakabon.github.io)

# karattebakabon.github.io

```markdown
![GitHub Pages](https://img.shields.io/badge/Live-Site-karattebakabon.github.io-0a0?logo=github)

# 空手チョップをもう一度。  
非公式・空手バカボンWebサイト

> “伝説の底が今、抜けた！”──大槻ケンヂ  
> ……を Web 上で再現してみたかった人が 2003 年から HTML を書き続けた結晶です。

---

## 🥋 このリポジトリは何？
GitHub Pages で公開している静的サイト  
<https://karattebakabon.github.io/>  
を構成する **生 HTML＋手書き CSS＋ほんのり CGI** 一式です。  
1980〜90 年代インディーズ界隈のテクノ・バンド「空手バカボン」に関する資料を（ほぼ）全部盛りしています。

* ディスコグラフィ / ライブ音源 / 未発表音源解説  
* 2000 年代前半テイスト全開の装飾（marquee や crosshair カーソルに胸アツ）  
* 日別アクセスカウンタ CGI（Perl）  
* RSS・サイトマップ・OGP など “現代っぽい気遣い” も少々

---

## 📂 主なディレクトリ

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

※ “HTML 全盛期っぽさ” 優先でネーミングがカオスですがご容赦を。

---

## 🛠️ 技術ネタ

| 項目           | 使っているもの／理由 |
| -------------- | -------------------- |
| フロント       | プレーン HTML4/HTML5 + 手書き CSS |
| UI スニペット  | [DragDealer.js](https://skidding.github.io/dragdealer/) |
| アクセス解析   | Google Analytics UA（レガシー！）+ Woopra |
| アクセスカウンタ| Perl CGI (`daycount/`) |
| デプロイ       | GitHub Pages (`main` ブランチ直配信) |
| CI             | `file-update-notification.yml` で更新通知を投げるだけ |

---

## 📜 ライセンス

* **サイト本文・解説テキスト**：Creative Commons BY-NC-SA 4.0  
* **コード（HTML/CSS/JS/CGI）**：MIT  
* **音源・画像・歌詞など第三者著作物**：各権利者に帰属

---

## 🙏 クレジット
* 空手バカボン（大槻ケンヂ／内田雄一郎／ケラリーノ・サンドロヴィッチ）  
* “ナゴム再生委員会” & UK PROJECT  
* そして 20 年近く更新を続けるすべてのファンに敬礼！  

> **空手チョップをもう一度。**  
> Push するたび、オーシャンより深いリスペクトを込めて。
```

↑リポジトリをGitingestでテキスト化して、OpenAI o3にマークダウン出力させたもの
