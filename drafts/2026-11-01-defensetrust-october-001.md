---
status: draft
audience: 企業 IT 主管、資安負責人（政府、金融、製造、跨國企業）
channel: 官網產品文章（亦可轉 EDM）
objective: 以 10 月微軟打擊網釣服務事件說明惡意網域快速更換，帶出 DefenseTrust 情資更新與阻擋機制，導向企業健檢
sources: ["entity-defensetrust", "issue-threat-intel-figures", "event-health-check-campaign", "official-news-058", "official-news-055"]
---

# ［待審］一年超過 10 億則釣魚訊息：惡意網域換得比黑名單快，你的防線跟得上嗎？

## 發布前輸入

- 讀者與營運情境：已有防火牆、但仍靠人工或久未更新黑名單的企業 IT 團隊。
- 產品與核准宣稱：DefenseTrust；只使用下方「引用與待確認」列出的核准口徑。
- 文章目標與 CTA：了解 DefenseTrust 產品頁；台灣區老客戶免費企業健檢（至 2026-12-31）。

## 文章草稿

10 月下旬，微軟公布一項打擊跨國網釣犯罪服務的行動：依美國聯邦法院命令，接管並重新導向 YAM Store、CoGUI 與 Iron Man 等地下服務使用的部分惡意網域。微軟統計，今年 1 月以來，犯罪者透過這些服務發送超過 10 億則網釣電子郵件及簡訊，鎖定 150 多國、逾 7.5 萬個組織；微軟也封鎖了超過 10 萬個詐騙網域。

10 萬個網域只是其中一次行動的數字。對企業來說，真正的問題是：**當釣魚網站與惡意網域不斷更換，你的阻擋名單多久更新一次？**

### 靜態黑名單，擋不住會換位置的攻擊

許多企業仍把黑名單手動輸入防火牆，或使用長時間未更新的清單。靜態清單只能擋下已知、而且還沒換掉的來源；當攻擊者以新網域、新 IP 重新出發，舊清單就失去時效。

### DefenseTrust：讓威脅情資真正落實到網路防護

UGUARD DefenseTrust 透過持續更新的 IP／Domain 威脅情資進行分類與比對，連線命中情資時，依企業設定的安全策略進行阻擋，並可從日誌掌握命中紀錄與處理結果。

- **情資最晚每小時更新**，DefenseTrust 每 3 分鐘請求一次最新情資
- **最新情資保持在百萬筆等級**，涵蓋 **224 個國家**
- **有效攔截超過 80% 已知惡意網站**，包括網路釣魚、惡意軟體下載、殭屍網路與 C&C 連線
- 依企業策略阻擋，並從日誌追查命中的 IP／Domain 與處理結果

威脅情資不只是「查得到」，而是要在員工點下連結的那一刻就派上用場。

### 下一步

想知道貴公司的網路環境還有哪些破口？UGUARD 提供台灣區老客戶免費企業健檢服務，涵蓋 WAN／LAN 架構與流量分析、DNS／防火牆／應用存取等項目，活動至 2026 年 12 月 31 日。

👉 了解 DefenseTrust：https://www.uguardnetworks.com/products/defensetrust
👉 預約企業健檢：［待確認 CTA 目的頁］

## 引用與待確認

| 內容 | 依據 | 狀態 |
|---|---|---|
| 微軟行動、10 億則訊息、150 國、7.5 萬組織、10 萬網域 | iThome〈資安週報 1019～1022〉2026-10-23（https://www.ithome.com.tw/news/179896），2026-11-01 讀取 | 二手報導；微軟原始公告未直接核對 |
| 情資最晚每小時更新、每 3 分鐘請求 | `claim-threat-intel-cadence`，[情資數字](../wiki/issues/threat-intel-figures.md) | approved_current |
| 百萬筆等級、224 個國家 | `claim-threat-intel-volume-current`、`claim-threat-intel-coverage` | approved_current |
| 攔截超過 80% 已知惡意網站 | `claim-defensetrust-block-rate` | approved_current |
| 分類比對→依策略阻擋→日誌 | [news/58](../wiki/sources/official-news-058.md) | source_reported |
| 攔截範圍（釣魚、惡意下載、殭屍網路、C&C） | [DefenseTrust](../wiki/entities/defensetrust.md) 功能表 | source_reported；產品確認 |
| 健檢活動與內容、期限 | `claim-health-check-campaign`，[健檢活動](../wiki/events/health-check-campaign.md) | approved_current；資格名額未確認 |
| 產品頁 URL | news/58 正確 CTA | 發布前點擊確認 |
| 健檢 CTA 目的頁 | 官網 sitemap 有 /enterpriseHealth，未讀取內容 | 待確認 |

避用：零誤判、零時差、不中斷、業界最快、徹底防堵（見 [時效及宣稱事項](../wiki/issues/time-sensitive-claims.md)）。
