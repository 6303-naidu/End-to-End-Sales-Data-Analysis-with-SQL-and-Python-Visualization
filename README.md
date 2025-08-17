# Sales Insights Project (SQL + Python)

## Overview
This project demonstrates how to build an end-to-end **Sales Insights Dashboard** using **SQL (SQLite)** and **Python**.  
It showcases **data storage, SQL queries, and business visualization** for decision-making.

## Dataset
- `customers.csv` → Customer info with region  
- `products.csv` → Product catalog with price & category  
- `sales.csv` → Sales transactions  

## Workflow
1. Load CSV data into SQLite (`init_db.py`)
2. Run SQL queries for insights (`queries.py`)
3. Generate business visualizations (`visualize.py`)

## Key Insights
- Top regions contributing to sales  
- Highest revenue-generating customers  
- Sales distribution by product category  

## Tech Stack
- SQL (SQLite)  
- Python (Pandas, Matplotlib, Seaborn)  
- VS Code  
## results
Top 3 Customers:
   customer_name  revenue
0     John Smith     2100
1    Michael Lee     1700
2  Sarah Johnson      950

Product Category Sales:
      category  category_sales
0  Electronics            5100
1    Furniture            1110
