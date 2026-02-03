CREATE TABLE products (
    product_id NUMBER PRIMARY KEY,
    product_name VARCHAR2(100),
    category VARCHAR2(50)
);

CREATE TABLE sales (
    sale_id NUMBER PRIMARY KEY,
    store_id NUMBER,
    product_id NUMBER,
    sale_date DATE,
    quantity NUMBER,
    price NUMBER,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(product_id)
);
