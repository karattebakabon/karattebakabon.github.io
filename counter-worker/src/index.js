// 空手バカボン アクセスカウンター Worker
// 死亡した ezcounter（today / yesterday / total）の代替。
// <img src="https://<worker>/count" ...> で呼ぶだけで計測＋数字SVG表示。
// CORS不要（img要素なので）。Cache-Control: no-store でブラウザキャッシュ抑止。

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // --- 日替わりキーの生成（JST固定。配信元が海外POPでも日本時間で日が変わる） ---
    const nowJST = new Date(Date.now() + 9 * 3600 * 1000);
    const dayKey = nowJST.toISOString().slice(0, 10); // "2026-09-06"

    // --- KV が未バインドなら簡易エラーSVG ---
    if (!env || !env.COUNTER) {
      return svg("NO KV");
    }

    const kv = env.COUNTER;

    // --- total 取得（未初期化なら 0） ---
    let total = parseInt((await kv.get("total")) || "0", 10);
    if (Number.isNaN(total)) total = 0;

    // --- today 取得＆更新 ---
    let today = parseInt((await kv.get(`d:${dayKey}`)) || "0", 10);
    if (Number.isNaN(today)) today = 0;
    today += 1;
    total += 1;

    // --- yesterday 取得（前日の日キーから読む。存在しなければ0） ---
    const yst = new Date(Date.now() + 9 * 3600 * 1000 - 24 * 3600 * 1000);
    const ystKey = yst.toISOString().slice(0, 10);
    let yesterday = parseInt((await kv.get(`d:${ystKey}`)) || "0", 10);
    if (Number.isNaN(yesterday)) yesterday = 0;

    // --- 書き込み ---
    ctx.waitUntil(Promise.all([
      kv.put(`d:${dayKey}`, String(today)),
      kv.put("total", String(total)),
    ]));

    // --- 古い日付データの掃除（当月より前を削除。KV 一覧は無料枠で十分） ---
    // preserve yesterday 用に前日分は残す。軽量に list 一致判定のみ。
    ctx.waitUntil(cleanOld(kv, dayKey.slice(0, 7)));

    // --- レトロ風SVG（ezcounter風 常点滅…はせずシンプルに） ---
    const svgOut = renderCounter(today, yesterday, total);
    return new Response(svgOut, {
      headers: {
        "Content-Type": "image/svg+xml; charset=utf-8",
        "Cache-Control": "no-store, max-age=0",
      },
    });
  },
};

// ---- 当月より古い d:YYYY-MM-DD を削除 ---------------------------------
async function cleanOld(kv, curMonth) {
  try {
    let cursor;
    do {
      const list = await kv.list({ prefix: "d:", cursor });
      for (const k of list.keys) {
        // d:2026-09-06 → 2026-09
        const month = k.name.slice(2, 9);
        if (month !== curMonth && month !== prevMonth(curMonth)) {
          await kv.delete(k.name);
        }
      }
      cursor = list.list_complete ? undefined : list.cursor;
    } while (cursor);
  } catch (e) {
    // 掃除はアクセサリーなので失敗しても無視
  }
}

function prevMonth(yyyymm) {
  const y = parseInt(yyyymm.slice(0, 4), 10);
  const m = parseInt(yyyymm.slice(5, 7), 10);
  const pm = m === 1 ? 12 : m - 1;
  const py = m === 1 ? y - 1 : y;
  return `${py}-${String(pm).padStart(2, "0")}`;
}

// ---- SVG 描画 ---------------------------------------------------------
// 背景: #102806（サイトのダークグリーン）・数字GIF風の枠線
function renderCounter(today, yesterday, total) {
  const digits = (n, w = 6) => String(n).padStart(w, "0");
  const cell = (label, num) => `
    <g>
      <text x="10" y="14" font-size="9" fill="#66ccff" font-family="monospace">${label}</text>
      <text x="10" y="30" font-size="14" fill="#FFFCA0" font-family="monospace" letter-spacing="1">${digits(num)}</text>
    </g>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="200" height="88" viewBox="0 0 200 88">
  <rect width="200" height="88" fill="#102806" stroke="#CCCCCC" stroke-dasharray="3 2"/>
  <g transform="translate(0,8)">${cell("TODAY", today)}</g>
  <g transform="translate(0,40)">${cell("YESTERDAY", yesterday)}</g>
  <g transform="translate(0,58)">${cell("TOTAL (since 2015-11-13 reset)", total)}</g>
</svg>`;
}

// ---- エラー時の簡易SVG ------------------------------------------------
function svg(msg) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="160" height="30"><rect width="160" height="30" fill="#102806"/><text x="6" y="20" font-size="11" fill="#DDDDDD" font-family="monospace">${msg}</text></svg>`;
}
