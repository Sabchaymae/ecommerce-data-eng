import pandas as pd
import random
from datetime import datetime, timedelta

products = {
    "Laptop": ("Electronics", 750),
    "Smartphone": ("Electronics", 500),
    "Headphones": ("Accessories", 80),
    "Mouse": ("Accessories", 25),
    "Keyboard": ("Accessories", 45),
    "Monitor": ("Electronics", 220),
    "Tablet": ("Electronics", 300),
    "Office Chair": ("Furniture", 180),
    "Desk": ("Furniture", 250),
    "Webcam": ("Accessories", 60),
}

cities = ["Rabat", "Casablanca", "Oujda", "Fes", "Marrakech", "Tangier", "Agadir"]

data = []

start_date = datetime(2026, 1, 1)

for order_id in range(1, 1001):
    product = random.choice(list(products.keys()))
    category, price = products[product]

    quantity = random.randint(1, 5)
    order_date = start_date + timedelta(days=random.randint(0, 273))

    data.append({
        "order_id": order_id,
        "date": order_date.strftime("%Y-%m-%d"),
        "product": product,
        "category": category,
        "quantity": quantity,
        "unit_price": price,
        "city": random.choice(cities)
    })

df = pd.DataFrame(data)

df.to_csv("data/sales.csv", index=False)

print("Dataset generated successfully!")
print(f"Number of rows: {len(df)}")
print(df.head())