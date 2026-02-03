from fastapi import APIRouter
from app.models import PredictRequest, PredictResponse
from app.ml.predict import predict

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
def predict_sale(request: PredictRequest):
    data = request.dict()
    prediction = predict(data)
    return {"predicted_sales": prediction}
