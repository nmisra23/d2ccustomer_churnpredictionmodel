# Error Analysis Report

## 1. Executive Summary of Diagnostic Metrics
The optimized XGBoost model uses a tactical decision threshold of **0.35** to actively skew performance toward catching high-risk customer turnover.

* **False Positives (FP):** 250 instances
* **False Negatives (FN):** 90 instances

---

## 2. Risk & Financial Impact Architecture

### False Positives (Type I Error)
* **Definition:** Model predicts a loyal customer will churn; business deploys retention plays unnecessarily.
* **Financial Impact:** Unnecessary degradation of profit margins. Distributing $20 retention discounts or credits to users who had no intention of leaving introduces cash dilution. 
* **Operational Strain:** Wastes account management bandwidth on highly stable accounts.

### False Negatives (Type II Error)
* **Definition:** Model fails to spot a customer planning to churn; no defensive action is taken.
* **Financial Impact:** Severe revenue loss. The business suffers the loss of the customer's Full Lifetime Value (LTV) and must spend $3x–5x more in Customer Acquisition Cost (CAC) to replace them in the market.

---

## 3. Deep-Dive Profile Analysis: 10 Core Exemplars

### False Positive Archetypes (Predicted Churn, Actually Retained)
1.  **CUST_0412:** High ticket volume (4 in 30 days) combined with a contract transition. However, their high historical tenure (48 months) created baseline friction preventing actual churn.
2.  **CUST_1109:** Experience a temporary 40% drop in platform usage due to internal corporate holidays. The model flagged this as an exit signal, but operational stability returned naturally.
3.  **CUST_0822:** A Month-to-Month contract customer with high monthly fees ($115). Flagged due to pricing sensitivity vectors, but stayed due to high workflow lock-in.
4.  **CUST_1450:** Opened 3 technical integration tickets within 10 days. Flagged as highly volatile, but once engineering resolved the bug, customer health normalized.
5.  **CUST_1901:** Sudden deletion of 2 sub-user accounts. Flagged as contraction/churn, but was simply an internal organizational cleanup.

### False Negative Archetypes (Predicted Retention, Actually Churned)
6.  **CUST_0045:** Zero logged support tickets and flawless usage telemetry. Churned silently overnight due to a direct competitive corporate buyout.
7.  **CUST_0711:** Two-Year contract holder with low monthly usage fluctuations. Broke contract terms abruptly and absorbed the early termination penalty due to severe budgetary constraints.
8.  **CUST_2218:** Perfect health scores, but experienced an unmonitored executive leadership change. The incoming decision-maker replaced our platform with their preferred historical stack.
9.  **CUST_1088:** Gradual, minute usage erosion (2% month-over-month over a long period). The model failed to trigger on this slow decay, which culminated in an exit.
10. **CUST_1604:** High contract tenure ($>36$ months) with steady telemetry, but encountered a critical, unresolved compliance blocker that forced an immediate system offboarding.