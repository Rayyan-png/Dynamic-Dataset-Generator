import pandas as pd
from faker import Faker
import random

fake = Faker()

# Attribute functions
def get_product_id():
    return fake.uuid4()

def get_product_name():
    return fake.word().capitalize() + " " + fake.word().capitalize()

def get_category():
    return fake.random_element(["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty", "Books"])

def get_price():
    return round(random.uniform(5, 1000), 2)

def get_stock_quantity():
    return random.randint(1, 500)

def get_supplier():
    return fake.company()

def get_manufacture_date():
    return fake.date_between(start_date='-2y', end_date='today')

def get_expiry_date():
    return fake.date_between(start_date='today', end_date='+2y') if random.choice([True, False]) else None

def get_rating():
    return round(random.uniform(1, 5), 1)

# Main data generation function
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "product_id": get_product_id(),
            "product_name": get_product_name(),
            "category": get_category(),
            "price": get_price(),
            "stock_quantity": get_stock_quantity(),
            "supplier": get_supplier(),
            "manufacture_date": get_manufacture_date(),
            "expiry_date": get_expiry_date(),
            "rating": get_rating(),
        })
    return pd.DataFrame(data)

# Generate and save the product data
# df = generate_data(500)
# df.to_csv("product_data.csv", index=False)

# print("Product data CSV file has been generated successfully!")
