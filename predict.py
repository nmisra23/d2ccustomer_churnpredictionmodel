import joblib
import pandas as pd
import sys


def run_inference():
    # 1. Load the saved deployment pipeline
    try:
        pipeline = joblib.load('model.pkl')
    except FileNotFoundError:
        print("Error: 'model.pkl' not found. Please run the training notebook first.")
        sys.exit(1)

    scaler = pipeline['scaler']
    model = pipeline['model']
    feature_cols = pipeline['features']
    threshold = pipeline['threshold']

    # 2. Sample unseen runtime record (Simulating a real customer)
    raw_inference_data = pd.DataFrame([{
        'tenure_months': 12,
        'monthly_charges': 85.50,
        'total_charges': 1026.00,
        'support_tickets_30d': 4,
        'usage_drop_percentage': 0.45,
        'paperless_billing': 1,
        'contract_type_One-Year': 0,
        'contract_type_Two-Year': 0
    }])

    # 3. Normalize features using the training metrics
    scaled_features = scaler.transform(raw_inference_data[feature_cols])

    # 4. Generate prediction based on the business threshold
    churn_probability = model.predict_proba(scaled_features)[:, 1][0]
    prediction = 1 if churn_probability >= threshold else 0

    print("\n=== Churn Inference Engine ===")
    print(f"Calculated Risk Score: {churn_probability * 100:.1f}%")
    print(f"Action Triggered:      {bool(prediction)} (Threshold: {threshold})")
    print("===============================\n")


if __name__ == "__main__":
    run_inference()