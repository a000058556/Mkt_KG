---
status: draft
audience: 一般企業 IT 人員、研究機構與學術單位
channel: Facebook／LinkedIn 社群貼文
objective: 以 10 月冒用研究機構名義的活動邀請釣魚為話題，提醒 IP／Domain 情資阻擋的價值，導向 DefenseTrust 產品頁
sources: ["entity-defensetrust", "writing-social-posts", "issue-facebook-cta", "official-news-058", "facebook-pfbid0AMmGpcRMbRVaJt5HDHR6Ap49giTEcmR8sXYGvPregZ75e8PrgB4LLGuPNoL3Ap1Vl"]
---

# ［待審］【📩 一封活動邀請信，也可能是釣魚陷阱】

## 發布前輸入

- 讀者與營運情境：常收到研討會、活動邀請的機構與企業。
- 產品與核准宣稱：DefenseTrust；不聲稱能阻擋所有釣魚，只說已知惡意網站。
- 文章目標與 CTA：了解 DefenseTrust 產品頁。

## 文章草稿

【📩 一封活動邀請信，也可能是釣魚陷阱】

10 月，思科 Talos 揭露有駭客冒用國內研究機構名義寄送活動邀請信，竄改海報上的 QR Code，再以仿冒 Google 登入頁面竊取帳號密碼與驗證資料。

釣魚信越寫越像真的，網域也一直在換。除了提高員工警覺，連線這一關也要守住。

UGUARD DefenseTrust 以持續更新的 IP / Domain 威脅情資比對每一條連線，命中後依企業策略阻擋，並從日誌掌握紀錄：

✓ 情資最晚每小時更新，每 3 分鐘請求最新情資
✓ 有效攔截超過 80% 已知惡意網站
✓ 涵蓋 224 個國家的威脅情資
✓ 命中紀錄與處理結果，日誌一目了然

讓威脅情資不只是「查得到」，更能真正落實到企業網路防護。

👉 了解更多 DefenseTrust
🔗 https://www.uguardnetworks.com/products/defensetrust

#UGUARD #DefenseTrust #ThreatIntelligence #Phishing #CyberSecurity #DomainReputation

## 引用與待確認

| 內容 | 依據 | 狀態 |
|---|---|---|
| Talos 揭露 UAT-11985 冒用研究機構寄送活動邀請、竄改 QR Code、仿冒 Google 登入頁（AiTM） | iThome〈資安週報 1019～1022〉2026-10-23（https://www.ithome.com.tw/news/179896） | 二手報導；Talos 原文未直接核對。正文刻意不點名被冒用機構 |
| 情資頻率、80%、224 國 | `claim-threat-intel-cadence`、`claim-defensetrust-block-rate`、`claim-threat-intel-coverage` | approved_current |
| 比對→策略阻擋→日誌 | [news/58](../wiki/sources/official-news-058.md)、[FB 貼文](../wiki/sources/facebook-threat-intelligence-update.md) 結構 | source_reported |
| CTA 連結 | 舊 FB 貼文曾誤連 TrafficShaper，見 [CTA issue](../wiki/issues/facebook-cta.md)；本稿用 DefenseTrust 產品頁 | 發布前點擊確認 |

寫作提醒：AiTM 網釣頁常使用新註冊網域，情資不一定已收錄；正文只寫「已知惡意網站」，不要暗示可擋下所有釣魚。結構沿用 [社群短文](../wiki/writing/social-posts.md) 的問句開頭→機制→勾選條列→CTA。
