-- Voorbeeld procedure: totale sales per product per maand
CREATE OR REPLACE PROCEDURE get_monthly_sales(
    p_month IN VARCHAR2,
    p_result OUT SYS_REFCURSOR
)
AS
BEGIN
    OPEN p_result FOR
    SELECT product_id, SUM(quantity) AS total_qty, SUM(quantity*price) AS total_revenue
    FROM sales
    WHERE TO_CHAR(sale_date, 'YYYY-MM') = p_month
    GROUP BY product_id;
END;
