import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os


# =========================
# Connexion PostgreSQL
# =========================
load_dotenv()
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

query = "SELECT * FROM sales;"

df = pd.read_sql(query, connection)

print(df.head())
print("\nNombre de lignes :", len(df))
print("\nColonnes :")
print(df.columns)


# =========================
# CA par ville
# =========================

revenue_by_city = (
    df.groupby("city")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCA par ville :")
print(revenue_by_city)

revenue_by_city.plot(kind="bar")

plt.title("Chiffre d'affaires par ville")
plt.xlabel("Ville")
plt.ylabel("Chiffre d'affaires")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# =========================
# CA mensuel
# =========================

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_revenue = (
    df.groupby(df["order_date"].dt.to_period("M"))["total_amount"]
    .sum()
)

print("\nCA mensuel :")
print(monthly_revenue)

monthly_revenue.plot(kind="line", marker="o")

plt.title("Évolution du chiffre d'affaires mensuel")
plt.xlabel("Mois")
plt.ylabel("Chiffre d'affaires")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# =========================
# CA par produit
# =========================

revenue_by_product = (
    df.groupby("product")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCA par produit :")
print(revenue_by_product)

revenue_by_product.plot(kind="bar")

plt.title("Chiffre d'affaires par produit")
plt.xlabel("Produit")
plt.ylabel("Chiffre d'affaires")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# =========================
# AOV
# =========================

aov = df["total_amount"].mean()

print("\nAverage Order Value (AOV) :", round(aov, 2))


# =========================
# Data Quality
# =========================

print("\nValeurs nulles par colonne :")
print(df.isnull().sum())

print("\nNombre de doublons :", df.duplicated().sum())

print("\nQuantités <= 0 :", (df["quantity"] <= 0).sum())
print("Prix <= 0 :", (df["unit_price"] <= 0).sum())
print("CA <= 0 :", (df["total_amount"] <= 0).sum())

df["calculated_total"] = df["quantity"] * df["unit_price"]

print(
    "\nLignes avec un CA incorrect :",
    (df["total_amount"] != df["calculated_total"]).sum()
)


# =========================
# Analyse métier
# =========================

best_product = revenue_by_product.idxmax()
best_product_revenue = revenue_by_product.max()

print("\nProduit avec le plus gros CA :", best_product)
print("CA :", best_product_revenue)


best_city = revenue_by_city.idxmax()
best_city_revenue = revenue_by_city.max()

print("\nVille avec le plus gros CA :", best_city)
print("CA :", best_city_revenue)


revenue_by_category = (
    df.groupby("category")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCA par catégorie :")
print(revenue_by_category)

best_category = revenue_by_category.idxmax()

print("\nCatégorie dominante :", best_category)


# =========================
# Contribution des produits
# =========================

product_contribution = (
    revenue_by_product / df["total_amount"].sum() * 100
).sort_values(ascending=False)

print("\nContribution des produits au CA (%) :")
print(product_contribution.round(2))

product_contribution.plot(kind="bar")

plt.title("Contribution des produits au chiffre d'affaires")
plt.xlabel("Produit")
plt.ylabel("Contribution (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# =========================
# KPI généraux
# =========================

total_revenue = df["total_amount"].sum()
total_orders = df["order_id"].nunique()
total_units = df["quantity"].sum()

print("\n========== KPI GÉNÉRAUX ==========")
print("CA total :", total_revenue)
print("Nombre de commandes :", total_orders)
print("Nombre d'unités vendues :", total_units)
print("AOV :", round(total_revenue / total_orders, 2))


print("\n========== TOP PERFORMERS ==========")
print("Meilleur produit :", best_product)
print("Meilleure ville :", best_city)
print("Catégorie dominante :", best_category)


# =========================
# Meilleur mois
# =========================

best_month = monthly_revenue.idxmax()
best_month_revenue = monthly_revenue.max()

print("\nMeilleur mois :", best_month)
print("CA du meilleur mois :", best_month_revenue)


# =========================
# Fermeture connexion
# =========================

connection.close()