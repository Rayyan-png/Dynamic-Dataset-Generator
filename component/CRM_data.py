from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_customer_id():
    return str(fake.uuid4())

def generate_name():
    return fake.name()

def generate_email():
    return fake.email()

def generate_phone():
    return fake.phone_number()

def generate_address():
    return fake.address()

def generate_company():
    return fake.company()

def generate_industry():
    return random.choice(["Retail", "Finance", "Healthcare", "Technology", "Education"])

def generate_last_contact_date():
    return fake.date_this_year()

def generate_contact_method():
    return random.choice(["Email", "Phone", "In-Person", "Chatbot", "Social Media"])

def generate_purchase_history():
    return random.randint(0, 20)

def generate_total_spent():
    return round(fake.random_number(digits=5), 2)

def generate_customer_rating():
    return round(random.uniform(1.0, 5.0), 1)

def generate_loyalty_status():
    return random.choice(["Bronze", "Silver", "Gold", "Platinum"])

def generate_preferred_product_category():
    return random.choice(["Electronics", "Clothing", "Home & Kitchen", "Books", "Health & Beauty"])

def generate_feedback_score():
    return random.randint(1, 10)

def generate_next_followup_date():
    return fake.date_between(start_date="today", end_date="+30d")

def generate_assigned_sales_rep():
    return fake.name()

def generate_crm_data(num_records=100):
    data = [
        {
            "customer_id": generate_customer_id(),
            "name": generate_name(),
            "email": generate_email(),
            "phone": generate_phone(),
            "address": generate_address(),
            "company": generate_company(),
            "industry": generate_industry(),
            "last_contact_date": generate_last_contact_date(),
            "contact_method": generate_contact_method(),
            "purchase_history": generate_purchase_history(),
            "total_spent": generate_total_spent(),
            "customer_rating": generate_customer_rating(),
            "loyalty_status": generate_loyalty_status(),
            "preferred_product_category": generate_preferred_product_category(),
            "feedback_score": generate_feedback_score(),
            "next_followup_date": generate_next_followup_date(),
            "assigned_sales_rep": generate_assigned_sales_rep(),
        } for _ in range(num_records)
    ]
    return pd.DataFrame(data)

# Sample usage
df_crm = generate_crm_data(10)
print(df_crm.head())
