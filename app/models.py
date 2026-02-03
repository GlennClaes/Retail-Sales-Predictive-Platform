from pydantic import BaseModel
from datetime import date

class PredictRequest(BaseModel):
    store_id: int
    product_id: int
    sale_date: date

class PredictResponse(BaseModel):
    predicted_sales: int
