import pandas as pd
import psycopg2

# Lire les données transformées
df = pd.read_csv("data/sales_clean.csv")

# Connexion à PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    port="5433",
    database="ecommerce",
    user="datauser",
    password="datapass"
)

cursor = connection.cursor()

# Insérer chaque ligne dans PostgreSQL
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO sales (
            order_id,
            order_date,
            product,
            category,
            quantity,
            unit_price,
            city,
            total_amount
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING;
        """,
        (
            row["order_id"],
            row["order_date"],
            row["product"],
            row["category"],
            row["quantity"],
            row["unit_price"],
            row["city"],
            row["total_amount"]
        )
    )

connection.commit()

cursor.close()
connection.close()

print("Data loaded successfully into PostgreSQL!")
print(f"Rows processed: {len(df)}")