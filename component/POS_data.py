from faker import Faker
import pandas as pd
import random

fake = Faker()

# Attribute-specific functions
def get_transaction_id():
    return fake.uuid4()

def get_store_id():
    return fake.random_int(min=1000, max=9999)

def get_cashier_id():
    return fake.random_int(min=100, max=999)

def get_customer_id():
    return fake.uuid4()

def get_product_id():
    return fake.uuid4()

def get_product_name():
    return fake.word()

def get_category():
    return fake.random_element(["Electronics", "Clothing", "Groceries", "Home & Kitchen", "Toys", "Books"])

def get_quantity():
    return fake.random_int(min=1, max=10)

def get_price_per_unit():
    return round(fake.random_number(digits=3) + fake.random_number(digits=2) / 100, 2)

def get_total_price():
    return round(fake.random_number(digits=4) + fake.random_number(digits=2) / 100, 2)

def get_payment_method():
    return fake.random_element(["Credit Card", "Debit Card", "Cash", "Mobile Payment"])

def get_transaction_date():
    return fake.date_this_year()

def get_transaction_time():
    return fake.time()

def get_discount_applied():
    return round(fake.random_number(digits=2) / 100, 2)

def get_tax_amount():
    return round(fake.random_number(digits=2) / 100, 2)

def get_final_amount():
    return round(fake.random_number(digits=4) + fake.random_number(digits=2) / 100, 2)

# Main data generation function
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        record = {
            "transaction_id": get_transaction_id(),
            "store_id": get_store_id(),
            "cashier_id": get_cashier_id(),
            "customer_id": get_customer_id(),
            "product_id": get_product_id(),
            "product_name": get_product_name(),
            "category": get_category(),
            "quantity": get_quantity(),
            "price_per_unit": get_price_per_unit(),
            "total_price": get_total_price(),
            "payment_method": get_payment_method(),
            "transaction_date": get_transaction_date(),
            "transaction_time": get_transaction_time(),
            "discount_applied": get_discount_applied(),
            "tax_amount": get_tax_amount(),
            "final_amount": get_final_amount(),
        }
        data.append(record)
    
    return pd.DataFrame(data)

# Generate sample POS data
# df_sample = generate_data(10)
# print(df_sample.head())

# # Save to CSV
# df_sample.to_csv("pos_data.csv", index=False)
