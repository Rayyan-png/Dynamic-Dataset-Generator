from faker import Faker
import pandas as pd
import random
from datetime import datetime

fake = Faker()

# Separate functions for each attribute
def generate_order_id():
    return fake.uuid4()

def generate_customer_id():
    return fake.uuid4()

def generate_order_date():
    return fake.date_this_year()

def generate_order_status():
    return random.choice(["Pending", "Shipped", "Delivered", "Cancelled"])

def generate_total_amount():
    return round(random.uniform(10, 5000), 2)

def generate_payment_method():
    return random.choice(["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash on Delivery"])

def generate_shipping_address():
    return fake.address()

def generate_billing_address():
    return fake.address()

def generate_delivery_date():
    return fake.date_between(start_date="-30d", end_date="today")

def generate_order_notes():
    return fake.sentence()

# Main data generation function
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        record = {
            "order_id": generate_order_id(),
            "customer_id": generate_customer_id(),
            "order_date": generate_order_date(),
            "order_status": generate_order_status(),
            "total_amount": generate_total_amount(),
            "payment_method": generate_payment_method(),
            "shipping_address": generate_shipping_address(),
            "billing_address": generate_billing_address(),
            "delivery_date": generate_delivery_date(),
            "order_notes": generate_order_notes(),
        }
        data.append(record)
    return pd.DataFrame(data)

# Generate sample data
df_sample = generate_data(10)
print(df_sample.head())
