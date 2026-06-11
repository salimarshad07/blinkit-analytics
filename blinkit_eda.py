# Python file content will be added from your local file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
from mysql.connector import Error

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'blinkit_analytics'
}

def connect_to_db():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_data(query):
    conn = connect_to_db()
    if conn:
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    return None

# EDA Analysis
print("Blinkit Analytics EDA")
print("=" * 50)

# Load data
customers = fetch_data("SELECT * FROM blinkit_customers")
orders = fetch_data("SELECT * FROM blinkit_orders")
products = fetch_data("SELECT * FROM blinkit_products")

print(f"Customers: {len(customers)} rows")
print(f"Orders: {len(orders)} rows")
print(f"Products: {len(products)} rows")
