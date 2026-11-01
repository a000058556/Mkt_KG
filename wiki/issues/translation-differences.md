---
schema_version: "1.0.0"
id: "issue-translation-differences"
type: "issue"
title: "紀錄：英日版翻譯差異"
summary: "英日版的反義、數量級、數字歸屬與增刪段落；以繁中為準，依決策 Q10 舊文章不修改。"
language: "zh-TW"
status: "historical_only"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["human-2026-11-01-009", "official-news-003", "official-news-004", "official-news-005", "official-news-006", "official-news-009", "official-news-010", "official-news-011", "official-news-012", "official-news-017", "official-news-018", "official-news-019", "official-news-020", "official-news-041", "official-news-045"]
related: ["issue-promotion-language", "issue-threat-intel-figures", "entity-x-view"]
---

# 紀錄：英日版翻譯差異

依 [決策 Q8](../../docs/DECISIONS.md)，Wiki 以繁中為準；本頁記錄英日網頁本身需要修正或確認的地方，不影響繁中引用。

## 影響語意的差異

| 來源 | 差異 |
|---|---|
| [news/5](../sources/official-news-005.md) | 繁中「UGUARD 情資不受零時差攻擊」，英文譯成 "is not protected from zero-day attacks"，語意相反 |
| [news/12](../sources/official-news-012.md) | 繁中「破億個 IP」，英文 over a billion、日文 10 億件以上，差一個數量級 |
| [news/20](../sources/official-news-020.md) | 數字歸屬不同：英文寫 13 類約 100 萬筆來自 Defense Cloud、600 萬筆來自開源／第三方 |
| [news/11](../sources/official-news-011.md) | 英文獨有 UGUARD 授予 AAEON 設備認證標章段落；英日內文日期 2024-10-12，繁中無；英文 NGWM 對繁中 NGFM |
| [news/6](../sources/official-news-006.md) | 繁中「每小時更新速度達到真正的防禦與零時差攻擊」語句斷裂，英日譯成 zero-latency attacks |
| [news/3](../sources/official-news-003.md) | 繁中「總公司」，英日只寫設立新加坡公司 |
| [news/9](../sources/official-news-009.md) | 英日多出 Innotel「18 年以上產業經驗」 |
| [news/45](../sources/official-news-045.md) | 繁中獨有產品說明段與主動防禦 AgileLink 條件，見 [news/45 差異](promotion-language.md) |

## 其他翻譯差異

- [news/18](../sources/official-news-018.md)：內文日期繁中 2025-03-10 台北、英文 2025-03-11 New Taipei City；英文未保留「零誤判」。
- [news/41](../sources/official-news-041.md)：英文把「最全面」「業界最快」改為 one of the…，語氣較保守。
- [news/19](../sources/official-news-019.md)：英文對 AI Assistant、[X-View](../entities/x-view.md) 的描述與繁中不同；官網連結改為 lnkd.in 短網址。
- [news/10](../sources/official-news-010.md)：英日感謝對象改為代理商與經銷夥伴；[news/17](../sources/official-news-017.md) 英文多出媒體出處、功能名稱不同；[news/4](../sources/official-news-004.md) 英日 hashtag 寫 #CYBERSEC2025。

## 處置

依 [決策 Q10](../../docs/DECISIONS.md)（[使用者確認](../sources/human-2026-11-01-009.md)），官網舊文章不修改。撰稿或對外引用英日舊文前先對照繁中與核准口徑，不要沿用上表的錯誤。數字問題另見 [情資數字](threat-intel-figures.md)。
