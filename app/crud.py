# app/crud.py

from sqlalchemy import text
from app.db import SessionLocal

def get_monthly_sales(month: str):
    """
    Roep een PLSQL procedure of SQL query aan om totale sales per product te krijgen.
    """
    session = SessionLocal()
    try:
        sql = text("""
            SELECT product_id, SUM(quantity) AS total_qty, SUM(quantity*price) AS total_revenue
            FROM sales
            WHERE strftime('%Y-%m', sale_date) = :month
            GROUP BY product_id
        """)
        result = session.execute(sql, {"month": month}).fetchall()
        return [{"product_id": r[0], "total_qty": r[1], "total_revenue": r[2]} for r in result]
    finally:
        session.close()
