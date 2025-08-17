import sqlite3
import pandas as pd

# Connect to SQLite
conn = sqlite3.connect("sales.db")

# Load CSV files
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
sales = pd.read_csv("sales.csv")

# Write to SQLite tables
customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
sales.to_sql("sales", conn, if_exists="replace", index=False)

print("Database created successfully!")
conn.close()
