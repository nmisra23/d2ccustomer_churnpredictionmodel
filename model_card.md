# Model Card: 60-Day Customer Churn Prediction System

## 1. Intended Use
* **Primary Purpose:** Identifies high-risk subscription accounts tracking to terminate or fail to renew services within the upcoming 60-day window.
* **Target Users:** Customer Success Managers (CSMs), Growth Marketing Ops, and Executive Retentions Frameworks.
* **Downstream Actions:** Automated targeted email playbooks, manual account reviews, and high-priority retention discounts.

## 2. Model Pipeline Architecture & Training Data
* **Model Class:** Extreme Gradient Boosting (XGBoost) Classifier.
* **Training Snapshot Base:** Historical customer usage logs, ticketing frequencies, transactional contract variants, and monthly billing metrics.
* **Input Features Trained:** `tenure_months`, `monthly_charges`, `total_charges`, `support_tickets_30d`, `usage_drop_percentage`, `paperless_billing`, `contract_type_One-Year`, `contract_type_Two-Year`.

## 3. Performance Summary
Evaluated against out-of-sample test matrices under an engineered operating threshold of **0.35**:

| Metric | Score Value |
| :--- | :--- |
| **Accuracy** | 85.8% |
| **Precision** | 71.2% |
| **Recall (Sensitivity)** | 77.5% |
| **F1-Score** | 74.2% |
| **ROC-AUC** | 88.7% |

## 4. Ethical Risks & Built-in Guardrails
* **Algorithmic Bias:** Credit and pricing features must not act as a proxy to systematically deny standard pricing adjustments or lower tiers of service to vulnerable demographic segments.
* **Socioeconomic Impacts:** Biased classification risks alienating tight-margin accounts by treating them as un-savable, reinforcing negative market sentiment.

## 5. Operational Constraints & Monitoring Protocols
* **When NOT to Use:** Do not use this model to evaluate customer lifecycle outcomes immediately following structural corporate mergers or wholesale pricing revamps.
* **Data Drift Window:** Model performance must be audited every quarter. If feature distributions deviate ($PSI > 0.2$), re-training must be forced using the updated trailing 90 days of execution logs.