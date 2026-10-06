import pandas as pd

# 1. Lire les données brutes
df = pd.read_csv("data/sales.csv")

print("Données avant transformation :")
print(df.head())

# 2. Convertir la date
df["date"] = pd.to_datetime(df["date"])

# 3. Supprimer les doublons
df = df.drop_duplicates()

# 4. Calculer le montant total de chaque commande
df["total_amount"] = df["quantity"] * df["unit_price"]

# 5. Renommer la colonne date
df = df.rename(columns={"date": "order_date"})

# 6. Sauvegarder les données transformées
df.to_csv("data/sales_clean.csv", index=False)

print("\nTransformation terminée !")
print(f"Nombre de lignes : {len(df)}")
print("\nDonnées après transformation :")
print(df.head())