import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

# 1. Total Sales by Region
query1 = '''
SELECT c.region, SUM(s.quantity * p.price) AS total_sales
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
GROUP BY c.region
ORDER BY total_sales DESC;
'''
print("\nTotal Sales by Region:")
print(pd.read_sql(query1, conn))

# 2. Top 3 Customers by Revenue
query2 = '''
SELECT c.customer_name, SUM(s.quantity * p.price) AS revenue
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY revenue DESC
LIMIT 3;
'''
print("\nTop 3 Customers:")
print(pd.read_sql(query2, conn))

# 3. Product Category Sales
query3 = '''
SELECT p.category, SUM(s.quantity * p.price) AS category_sales
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.category;
'''
print("\nProduct Category Sales:")
print(pd.read_sql(query3, conn))

conn.close()
