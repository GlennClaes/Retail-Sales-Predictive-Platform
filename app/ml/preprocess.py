import pandas as pd

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # Zorg dat sale_date een string is (komt uit Pydantic als date object)
    df['sale_date'] = df['sale_date'].astype(str)
    df['sale_date'] = pd.to_datetime(df['sale_date'], dayfirst=False)
    df['day_of_week'] = df['sale_date'].dt.dayofweek
    df['month'] = df['sale_date'].dt.month
    return df[['store_id', 'product_id', 'day_of_week', 'month']]
