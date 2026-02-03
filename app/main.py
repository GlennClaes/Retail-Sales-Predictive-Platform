from fastapi import FastAPI
from app.routers import sales

app = FastAPI(title="Retail Sales Predictive Platform")
app.include_router(sales.router, prefix="/sales")
