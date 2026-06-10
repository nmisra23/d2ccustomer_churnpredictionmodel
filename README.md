# Customer Churn Prediction Pipeline (60-Day Horizon)

This repository contains an end-to-end Machine Learning system optimized to predict subscription accounts vulnerable to churning over a forward-looking 60-day operational window.

## 🚀 System Architecture Layout
* `churn_model.ipynb` - End-to-end data processing, feature verification, training, and evaluation notebook.
* `model.pkl` - Serialized final model pipeline object containing the scaling maps and optimized model parameters.
* `metrics.json` - Out-of-sample key performance metrics and data matrices.
* `error_analysis.md` - Technical breakdown of False Positives and False Negatives with 10 exact case histories.
* `model_card.md` - Enterprise-facing governance overview documenting constraints, ethics, and performance benchmarks.
* `requirements.txt` - Fixed dependency library requirements.

## 🛠️ Step-by-Step Production Execution Blueprint

### 1. Initialize and Setup Local Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook churn_predict_model.ipynb