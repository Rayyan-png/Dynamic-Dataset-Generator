from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_customer_id():
    return str(fake.uuid4())

def generate_customer_name():
    return fake.name()

def generate_age():
    return random.randint(18, 90)

def generate_gender():
    return random.choice(["Male", "Female", "Other"])

def generate_email():
    return fake.email()

def generate_phone_number():
    return fake.phone_number()

def generate_address():
    return fake.address()

def generate_city():
    return fake.city()

def generate_state():
    return fake.state()

def generate_country():
    return fake.country()

def generate_postal_code():
    return fake.postcode()

def generate_registration_date():
    return fake.date_this_decade()

def generate_last_purchase_date():
    return fake.date_between(start_date="-1y", end_date="today")

def generate_loyalty_points():
    return random.randint(0, 10000)

def generate_preferred_payment_method():
    return random.choice(["Credit Card", "Debit Card", "PayPal", "Bank Transfer"])

def generate_customer_segment():
    return random.choice(["Regular", "VIP", "Wholesale", "Online-Only"])

def generate_subscription_status():
    return random.choice(["Active", "Inactive", "Cancelled"])

def generate_total_spent():
    return round(random.uniform(100.00, 1000000.00), 2)

def generate_feedback_score():
    return random.randint(1, 5)

def generate_referral_source():
    return random.choice(["Social Media", "Friend", "Advertisement", "Search Engine"])

def generate_customer_data(num_records=100):
    data = [
        {
            "customer_id": generate_customer_id(),
            "customer_name": generate_customer_name(),
            "age": generate_age(),
            "gender": generate_gender(),
            "email": generate_email(),
            "phone_number": generate_phone_number(),
            "address": generate_address(),
            "city": generate_city(),
            "state": generate_state(),
            "country": generate_country(),
            "postal_code": generate_postal_code(),
            "registration_date": generate_registration_date(),
            "last_purchase_date": generate_last_purchase_date(),
            "loyalty_points": generate_loyalty_points(),
            "preferred_payment_method": generate_preferred_payment_method(),
            "customer_segment": generate_customer_segment(),
            "subscription_status": generate_subscription_status(),
            "total_spent": generate_total_spent(),
            "feedback_score": generate_feedback_score(),
            "referral_source": generate_referral_source(),
        } for _ in range(num_records)
    ]
    return pd.DataFrame(data)

# Sample usage
df_customers = generate_customer_data(10)
print(df_customers.head())
