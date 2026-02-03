import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Zorg dat model folder bestaat
os.makedirs("../../models", exist_ok=True)

# Load data
df = pd.read_csv("../../data/historical_sales.csv", sep=None, engine='python')
print("Kolommen in CSV:", df.columns.tolist())

# Kolommen opschonen
df.columns = df.columns.str.strip().str.lower()

# Datum correct instellen
df['sale_date'] = pd.to_datetime(df['sale_date'], dayfirst=True)

# Feature engineering
df['day_of_week'] = df['sale_date'].dt.dayofweek
df['month'] = df['sale_date'].dt.month

features = ['store_id', 'product_id', 'day_of_week', 'month']
X = df[features]
y = df['quantity']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "../../models/sales_model.pkl")
print("Model saved as sales_model.pkl")
