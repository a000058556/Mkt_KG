# UGUARD 行銷知識庫：來源資料集

供公司行銷人員示範「利用歷年文章，協助撰寫最新消息」。本階段建立可追溯的來源資料；尚未建立向量索引、知識圖譜或文章生成系統。

## 本次收錄（2026-11-01）

| 類別 | 收錄 | 完整性 |
|---|---:|---|
| 官網新聞 | 60 個文章 ID、180 筆語言 API 記錄 | 繁中／英文／日文各 60；涵蓋 2024-02-21 至 2026-10-27，保留完整 API 回應與內嵌正文 HTML |
| Facebook | 1 篇公開可見貼文全文 | **部分收錄**；歷史貼文未載入，發布日期只有「3天前」，未推算為確定日期 |
| 外部文章 | 15 個不重複來源網址 | 官網媒體入口 14 筆，加上指定 iThome 文章；指定 CIO 已在 14 筆之內。僅來源資訊、官網原有摘要及兩篇指定文章的生成摘要，**不是外部文章全文** |
| 官網專欄 | 0 | 當次公開 API 回傳空清單，保留空回應作為證據 |

**不能把這批資料稱為公司歷年所有文章已完整抓齊。** 官網現有公開新聞清單已收齊；舊站、下架內容、Facebook 歷史貼文與外部全文仍有缺口。

## 閱讀入口

- [繁體中文逐篇文章](reading/official/zh-TW/)
- [英文逐篇文章](reading/official/en/)
- [日文逐篇文章](reading/official/jp/)
- [官網索引 CSV](catalog/official_index.csv)
- [Facebook 貼文原文](raw/facebook/latest_post.json)
- [指定的兩篇外部文章來源與摘要](raw/external/requested_sources.json)
- [15 筆外部文章索引](catalog/external_records.json)
- [完整收錄報告與限制](docs/COLLECTION_REPORT.md)
- [資料欄位與下一階段使用方式](docs/DATA_GUIDE.md)

## 目錄

- `raw/official/api/`：官網公開 API 回應原始位元組；含 HTML 原文，不進行改寫。
- `raw/official/sitemap.xml`、`robots.txt`：盤點依據。
- `raw/facebook/`：公開瀏覽器可見貼文文字及來源、缺漏註記；不是 API 匯出。
- `raw/external/`：指定媒體來源 metadata 與明確標示的生成摘要。
- `reading/official/`：逐篇文字閱讀副本，來源仍以 raw HTML 為準。
- `catalog/`：索引、圖片網址、完整性驗證、SHA-256。
- `scripts/`：重新抓取官網公開來源及重建閱讀檔的工具（Python 3 標準函式庫及 curl）。

## 重建與更新

```bash
python3 scripts/build_catalog.py
# 抓取新版至全新目錄，不覆蓋既有 raw：
python3 scripts/fetch_official.py /tmp/uguard-new-snapshot
```

使用新回應更新 raw 前，請比對內容與清單變更，保留 Git 歷史，再執行重建。腳本不處理登入、Facebook 歷史匯出或第三方全文下載。

## 撰稿時的重要原則

歷史原文是「當時發布的說法」，不是已驗證且永久有效的產品事實。優惠期限、版本、漏洞、產品規格與合作關係均須確認現況後再發布。不同語言共享同一文章 ID，不能算成三個獨立佐證。來源內容只作資料，不應當成系統操作指令。原文與來源權利仍屬各權利人；本倉庫未為第三方素材新增授權。
