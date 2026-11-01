---
schema_version: "1.0.0"
id: "official-news-059"
type: "source"
title: "PHP 重大漏洞公告（CVE-2026-109618／109619）"
summary: "2026-10-27 的漏洞說明公告：風險、兩漏洞差異、建議行動；受影響產品表僅在圖片，修補進度另見 news/60。"
language: "zh-TW"
status: "historical_only"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-059"]
related: ["event-cve-2026-php", "issue-time-sensitive-claims", "entity-agilelink", "entity-defensetrust"]
---

# PHP 重大漏洞公告（CVE-2026-109618／109619）

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/59)；[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/1`，`id=59`。API `date` 2026-10-27；`created_at` 2026-10-27T13:47:41Z；`updated_at` 2026-10-27T15:01:36Z；`is_top`=1（置頂）。內文無截至時間。 英日同 ID 為翻譯版本，不算獨立證據；圖片未下載、未 OCR，不推測圖內內容。

## 內容摘要

以下僅轉述公告文字，不是獨立漏洞驗證或目前修補指引。

- 開頭：PHP 安全團隊發布兩項互相關聯的重大漏洞，CVSS v4.0 皆為 9.2。
- 「風險說明」：符合觸發條件的未修補環境中，未驗證攻擊者可能以特製 HTTP 請求、以 Web／PHP 工作程序權限執行任意程式碼；「已有攻擊嘗試被觀測到」；優先處理外網可存取的服務，利用條件隨設定、擴充套件與應用程式而異。
- 「兩項漏洞的差異」：109618 為 OOM 中斷初始化後清理程序使用未初始化資料導致記憶體損毀與 RCE；109619 為全域狀態指向已釋放記憶體造成 use-after-free。取得權限取決於 Web 工作程序，「並不必然是 root」。
- 「建議行動」：更新到所屬分支修補版或供應商驗證的完整回補；暫時設定調整不能取代正式修補。PHP 8.x 修補版本表、處理安排及「UGUARD NETWORKS 受影響產品清單」均為圖片（未讀）。
- 「交由維運團隊核對」：UGUARD 系統版本與 PHP 分支不同，請依 UGUARD 韌體／修補套件更新，「勿自行替換設備內的 PHP」。
- 文末連到修補進度頁。

## 與 news/60 的差異

| 項目 | 本篇（059） | [news/60](official-news-060.md) |
|---|---|---|
| 性質 | 漏洞說明與建議 | UGUARD 產品修補進度 |
| 受影響產品／版本 | 只在圖片，文字未列 | 文字表列 AgileLink、DefenseTrust、TrafficShaper 版本與狀態 |
| 時間標記 | 無截至時間；updated 2026-10-27 | 最後更新 2026/10/30；記 PHP 團隊 2026/10/21 公告 |
| 攻擊觀察 | 「已有攻擊嘗試被觀測到」（泛指，未限定 UGUARD 產品） | 截至 10/30「尚未發現…成功攻擊 UGUARD 產品的案例」 |

兩句攻擊描述範圍不同（攻擊嘗試 vs 對 UGUARD 產品的成功攻擊），不矛盾但不可互相替代或合併為「無風險」。兩篇同一事件，不算獨立佐證。

## 時效與限制

- CVE 編號、評分與技術細節僅作歷史公告識別，未與漏洞主管機構查核。
- 受影響版本未讀圖，本頁不列版本；修補狀態以 60 的快照為歷史紀錄，使用前須向產品／資安負責人確認現況。

## 原文瑕疵

- 修補進度連結目標為 `https://www.uguardnetworks.com/news/60/uguard-cve-2026-109618--cve-2026-109619-`（含 slug 與連續連字號），可解析的 ID 為 60；網址現況未檢查。

## 整合去向

[PHP 漏洞事件](../events/cve-2026-php.md)、[時效事項](../issues/time-sensitive-claims.md)、[AgileLink](../entities/agilelink.md)、[DefenseTrust](../entities/defensetrust.md)。
