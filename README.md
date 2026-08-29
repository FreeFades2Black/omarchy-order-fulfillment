# 📦 Omarchy Multi-Warehouse Order Fulfillment Engine

Distributed logistics routing and automated order dispatch microservice migrated from Azure DevOps to GitHub Enterprise.

---

## 📋 Migration & Governance Audit

* **Source Platform:** Azure DevOps (`source-ado-repos/omarchy-order-fulfillment`)
* **Target Platform:** GitHub Enterprise (`FreeFades2Black/omarchy-order-fulfillment`)
* **Pipeline Translation:** Converted legacy `azure-pipelines.yml` to native GitHub Actions `.github/workflows/ci.yml`.
* **Compliance Verdict:** `PASSED_100_PERCENT_PARITY`
* **Secret Scan:** `CLEAN` (0 exposed credentials in git history).

---

## 🚀 API Endpoints

* `GET /health` — Service health & logistics queue status.
* `POST /api/orders/dispatch` — Assigns fulfillment centers and generates tracking manifests.

---

## 🛠️ Local Development

```bash
# Run service locally
python3 -m uvicorn app:app --host 0.0.0.0 --port 8840
```
