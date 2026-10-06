import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port=5433,
    database="ecommerce",
    user="datauser",
    password="datapass"
)

print("Connexion PostgreSQL réussie !")

connection.close()