---
status: draft
audience: 既有客戶與通路夥伴的 IT／資安主管（製造、關鍵基礎設施、跨國企業）
channel: 客戶 EDM／電子報
objective: 以 10 月 APT28 HookEdge 後門建立反向連線的案例，說明監控與阻擋異常外連的重要性，導向 DefenseTrust 與汰舊換新方案
sources: ["entity-defensetrust", "concept-ngfw-complement", "concept-legacy-replacement", "official-news-054", "official-news-034", "official-news-045"]
---

# ［待審］入侵之後，電腦會「主動打電話回家」：你看得見異常的外連嗎？

## 發布前輸入

- 讀者與營運情境：已部署防火牆、重視內網安全，但缺乏對外連線可視性的企業。
- 產品與核准宣稱：DefenseTrust；不聲稱能偵測或阻止特定後門，只說比對已知惡意 IP／Domain 與異常外部連線。
- 文章目標與 CTA：洽詢 DefenseTrust；舊機型客戶的汰舊換新方案。

## 文章草稿

**許多攻擊不是從外面硬闖進來，而是讓裡面的電腦自己連出去。**

10 月，資安業者 Symantec 揭露俄羅斯駭客組織 APT28 攻擊北約成員國的造船企業等單位：員工開啟含惡意巨集的 Word 文件後，電腦遭植入 HookEdge 後門；攻擊者再利用 Windows 內建工具，讓受害電腦**主動連向外部伺服器**，建立 SSH 反向通道，從外部存取企業內網。

這類攻擊的關鍵在於「由內往外」的連線。若只防守進來的流量，往外的連線就可能被放行。

### 把外連也納入防線

UGUARD DefenseTrust 可作為次世代防火牆的好幫手：在連線前段以全球威脅情資比對 IP 與 Domain，命中已知惡意來源時依策略阻擋，減輕防火牆的工作負擔，讓防火牆專注於更複雜的威脅分析。

- **偵測異常外部（C&C）連線**：比對連線目的地是否為已知惡意 IP／Domain
- **情資持續更新**：情資最晚每小時更新，DefenseTrust 每 3 分鐘請求最新情資；最新情資保持在百萬筆等級，涵蓋 224 個國家
- **日誌可追查**：命中的 IP／Domain、連線狀況與處理結果，都能從日誌查看，協助事後調查

### 舊設備也該一起升級

如果貴公司仍在使用 UGUARD 舊機型，汰舊換新升級方案仍在進行中：購買 2 年（含）以上保固加贈 1 年，並享原廠兩次免費企業健檢（限保固第一年使用），活動至 2027 年 12 月 25 日。

📞 業務聯絡：［待確認電話與信箱］
👉 了解 DefenseTrust：https://www.uguardnetworks.com/products/defensetrust

## 引用與待確認

| 內容 | 依據 | 狀態 |
|---|---|---|
| APT28、HookEdge、Word 惡意巨集、主動外連、SSH 反向通道 | iThome〈資安週報 1019～1022〉2026-10-23（https://www.ithome.com.tw/news/179896），引述 Symantec | 二手報導；Symantec 原文未直接核對。受害者為北約成員國企業，正文未暗示台灣受害 |
| 偵測異常外部（C&C）連線 | [news/54](../wiki/sources/official-news-054.md) 應用情境 | source_reported；產品確認 |
| 防火牆好幫手、減輕負擔 | `claim-ngfw-offload`，[補強 NGFW](../wiki/concepts/ngfw-complement.md) | source_reported |
| 情資頻率、百萬筆、224 國 | `claim-threat-intel-cadence`、`claim-threat-intel-volume-current`、`claim-threat-intel-coverage` | approved_current |
| 日誌內容 | [news/58](../wiki/sources/official-news-058.md) | source_reported |
| 汰舊換新仍在辦、期限 2027-12-25 | `claim-tradein-promotion` | approved_current |
| 禮遇內容（2+1 年保固、兩次健檢限保固第一年）與適用舊機型 | [news/45](../wiki/sources/official-news-045.md) 汰舊換新段 | 條件細節未另確認，發布前請業務核對 |
| 業務聯絡方式 | news/45 曾列 (02) 8226-1068 / sales 信箱 | 待確認現行窗口 |

寫作提醒：DefenseTrust 依情資比對已知惡意目的地，攻擊者若使用尚未收錄的新伺服器，不一定能命中；不要寫成「可阻止 HookEdge」或「防止所有反向通道」。
