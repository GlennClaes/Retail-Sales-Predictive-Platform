# app/routers/dashboard.py

from fastapi import APIRouter
from app.crud import get_monthly_sales

router = APIRouter()

@router.get("/monthly-sales/{month}")
def monthly_sales(month: str):
    """
    Geef een overzicht van de sales per product voor een specifieke maand (YYYY-MM)
    """
    data = get_monthly_sales(month)
    return {"month": month, "sales": data}
