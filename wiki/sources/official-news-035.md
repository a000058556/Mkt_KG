---
schema_version: "1.0.0"
id: "official-news-035"
type: "source"
title: "Traffic Shaper：雲端與 AI 時代的網路管理"
summary: "介紹 Traffic Shaper 的 L7 應用辨識、頻寬分配、儀表板與 Inline／SPAN 部署及 Bypass 設計。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-035"]
related: ["entity-trafficshaper", "concept-traffic-management", "writing-product-article"]
---

# Traffic Shaper：雲端與 AI 時代的網路管理

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/35)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/25`，`id=35`。

- API `date`：2025-12-18
- `created_at`／`updated_at`：皆 2026-05-25T14:45:44Z
- 內文日期：健檢活動「即日起至 2026 年 12 月 31 日」

## 內容摘要

依正文各段：

- **開頭**：SaaS、雲端、視訊會議與 AI 應用使流量問題不只是速度，而是關鍵服務保障、使用可視與異常追蹤；只靠防火牆或升級頻寬難以因應。
- **核心功能**：Layer 7 應用辨識與流量管理，掌握「誰在什麼時間，使用了哪些應用與服務」；可依使用者、群組、應用、網站類型分配與控管頻寬。
- **儀表板**：L7 QoS 即時呈現各應用流量、上傳／下載趨勢、熱門服務排名與分佈；整合設備狀態、CPU、記憶體、連線數，即時顯示 Top 10 Domain 與服務流量占比；搭配使用者身分辨識與認證。
- **部署模式**（小標「Traffic Shaper 產品簡單化部屬模式」）：支援 Inline 與 SPAN 模式，提供硬體式與軟體式 Bypass，原文稱「確保營運不中斷」。
- **健檢活動**：重複至 2026-12-31 的老客戶健檢段落，附活動頁連結；另有 `tw.uguardnetworks.com/traffic-shaper/` 產品頁連結。

## 時效與限制

- 「確保營運不中斷」「關鍵利器」為宣傳語；Bypass 行為未附切換條件或規格。
- 功能描述為 2025-12 來源說法，未對照現行版本。
- 健檢活動以 2026-11-01 評估尚未到截止日，需業務確認。
- 圖片 `tOS-dashboard-ui.jpg`、`tOS-mode-info.jpg` 未檢視。

## 原文瑕疵

- 「部屬」應為「部署」（同段正文寫「部署」）；同樣小標亦見 [official-news-008](official-news-008.md) 標題。

## 整合去向

[Traffic Shaper](../entities/trafficshaper.md)、[頻寬與流量管理](../concepts/traffic-management.md)、[產品文章寫法](../writing/product-article.md)。
