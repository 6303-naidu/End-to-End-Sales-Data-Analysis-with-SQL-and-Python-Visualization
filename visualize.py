import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales.db")

# Sales by Region
df_region = pd.read_sql('''
SELECT c.region, SUM(s.quantity * p.price) AS total_sales
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
GROUP BY c.region;
''', conn)

# Plot
plt.bar(df_region['region'], df_region['total_sales'])
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.show()

# Category Sales
df_category = pd.read_sql('''
SELECT p.category, SUM(s.quantity * p.price) AS total_sales
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.category;
''', conn)

df_category.plot(kind="pie", y="total_sales", labels=df_category["category"], autopct="%1.1f%%", legend=False)
plt.title("Sales by Product Category")
plt.show()

conn.close()
