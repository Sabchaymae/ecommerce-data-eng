CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    product VARCHAR(100),
    category VARCHAR(100),
    quantity INTEGER,
    unit_price NUMERIC(10,2),
    city VARCHAR(100),
    total_amount NUMERIC(10,2)
);