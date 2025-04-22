import pandas as pd
from faker import Faker
import random
from datetime import datetime

fake = Faker()

# Individual attribute generators
def get_transaction_id():
    return fake.uuid4()

def get_amount():
    return round(random.uniform(10, 10000), 2)

def get_currency():
    return fake.currency_code()

def get_transaction_date():
    return fake.date_time_this_year()

def get_payment_method():
    return random.choice(["Credit Card", "Debit Card", "Bank Transfer"])

def get_account_number():
    return fake.iban()

def get_customer_id():
    return fake.uuid4()

def get_merchant_name():
    return fake.company()

def get_transaction_status():
    return random.choice(["Completed", "Pending", "Failed"])

def get_country():
    return fake.country()

def get_city():
    return fake.city()

def get_zip_code():
    return fake.zipcode()

def get_reference_number():
    return fake.bothify("??###-###")

def get_card_type():
    return fake.credit_card_provider()

def get_card_expiry():
    return fake.credit_card_expire()

def get_fraud_flag():
    return random.choice([True, False])

def get_exchange_rate():
    return round(random.uniform(0.5, 1.5), 4)

def get_fee_amount():
    return round(random.uniform(1, 50), 2)

def get_refund_status():
    return random.choice(["None", "Partial", "Full"])

def get_branch_code():
    return random.randint(10000, 99999)

# Main generator using modular attribute functions
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "transaction_id": get_transaction_id(),
            "amount": get_amount(),
            "currency": get_currency(),
            "transaction_date": get_transaction_date(),
            "payment_method": get_payment_method(),
            "account_number": get_account_number(),
            "customer_id": get_customer_id(),
            "merchant_name": get_merchant_name(),
            "transaction_status": get_transaction_status(),
            "country": get_country(),
            "city": get_city(),
            "zip_code": get_zip_code(),
            "reference_number": get_reference_number(),
            "card_type": get_card_type(),
            "card_expiry": get_card_expiry(),
            "fraud_flag": get_fraud_flag(),
            "exchange_rate": get_exchange_rate(),
            "fee_amount": get_fee_amount(),
            "refund_status": get_refund_status(),
            "branch_code": get_branch_code(),
        })
    return pd.DataFrame(data)

# Generate and show sample data
df_sample = generate_data(10)
print(df_sample.head())
