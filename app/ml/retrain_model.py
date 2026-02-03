import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Pad instellingen
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "historical_sales.csv")
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "sales_model.pkl")

# Load data
df = pd.read_csv(DATA_PATH)

# Preprocessing
df['sale_date'] = pd.to_datetime(df['sale_date'], dayfirst=False)
df['day_of_week'] = df['sale_date'].dt.dayofweek
df['month'] = df['sale_date'].dt.month

features = ['store_id', 'product_id', 'day_of_week', 'month']
X = df[features]
y = df['quantity']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, MODEL_PATH)
print("Retrained model saved at:", MODEL_PATH)
