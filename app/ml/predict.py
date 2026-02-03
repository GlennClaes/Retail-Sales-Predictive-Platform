import os
import pandas as pd
import joblib
from app.ml.preprocess import preprocess

# Bepaal project root en model path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "sales_model.pkl")

# Laad model bij import
model = joblib.load(MODEL_PATH)

def predict(data: dict):
    # Zet JSON dict om naar DataFrame
    df = pd.DataFrame([data])
    X = preprocess(df)
    # Check wat er naar het model gaat
    print("Features for prediction:\n", X)
    pred = model.predict(X)
    return int(pred[0])
