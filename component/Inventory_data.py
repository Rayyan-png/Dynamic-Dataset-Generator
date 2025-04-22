from faker import Faker
import pandas as pd
import random

fake = Faker()

# Separate functions for each attribute
def generate_inventory_id():
    return str(fake.uuid4())

def generate_product_name():
    return fake.word()

def generate_product_category():
    return random.choice(["Electronics", "Clothing", "Groceries", "Furniture", "Toys"])

def generate_quantity_available():
    return fake.random_int(min=0, max=1000)

def generate_warehouse_location():
    return fake.city()

def generate_supplier_name():
    return fake.company()

def generate_supplier_contact():
    return fake.phone_number()

def generate_last_restocked_date():
    return fake.date_this_year()

def generate_expiration_date():
    return fake.date_between(start_date="+30d", end_date="+365d")

def generate_cost_per_unit():
    return round(random.uniform(1, 500), 2)

def generate_selling_price():
    return round(random.uniform(10, 1000), 2)

def generate_reorder_level():
    return fake.random_int(min=10, max=500)

def generate_stock_status():
    return random.choice(["In Stock", "Out of Stock", "Low Stock"])

# Main function to generate dataset
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "inventory_id": generate_inventory_id(),
            "product_name": generate_product_name(),
            "product_category": generate_product_category(),
            "quantity_available": generate_quantity_available(),
            "warehouse_location": generate_warehouse_location(),
            "supplier_name": generate_supplier_name(),
            "supplier_contact": generate_supplier_contact(),
            "last_restocked_date": generate_last_restocked_date(),
            "expiration_date": generate_expiration_date(),
            "cost_per_unit": generate_cost_per_unit(),
            "selling_price": generate_selling_price(),
            "reorder_level": generate_reorder_level(),
            "stock_status": generate_stock_status(),
        })
    return pd.DataFrame(data)

# Generate and display sample data
df_sample = generate_data(10)
print(df_sample.head())

# # Save to CSV
# df_sample.to_csv("inventory_data.csv", index=False)
