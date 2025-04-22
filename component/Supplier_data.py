from faker import Faker
import pandas as pd
import random

fake = Faker()

# Define individual attribute generator functions
def generate_supplier_id():
    return str(fake.uuid4())

def generate_company_name():
    return fake.company()

def generate_contact_name():
    return fake.name()

def generate_email():
    return fake.email()

def generate_phone_number():
    return fake.phone_number()

def generate_address():
    return fake.address()

def generate_city():
    return fake.city()

def generate_country():
    return fake.country()

def generate_postal_code():
    return fake.postcode()

def generate_website():
    return fake.url()

def generate_product_category():
    return fake.random_element(elements=["Electronics", "Clothing", "Groceries", "Furniture", "Pharmaceuticals"])

def generate_contract_start_date():
    return fake.date_this_decade()

def generate_contract_end_date():
    return fake.date_this_decade() if fake.boolean(chance_of_getting_true=70) else None

def generate_payment_terms():
    return fake.random_element(elements=["Net 30", "Net 60", "Net 90"])

def generate_rating():
    return random.randint(1, 5)

# Master function to generate dataset
def generate_supplier_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "supplier_id": generate_supplier_id(),
            "company_name": generate_company_name(),
            "contact_name": generate_contact_name(),
            "email": generate_email(),
            "phone_number": generate_phone_number(),
            "address": generate_address(),
            "city": generate_city(),
            "country": generate_country(),
            "postal_code": generate_postal_code(),
            "website": generate_website(),
            "product_category": generate_product_category(),
            "contract_start_date": generate_contract_start_date(),
            "contract_end_date": generate_contract_end_date(),
            "payment_terms": generate_payment_terms(),
            "rating": generate_rating(),
        })
    
    return pd.DataFrame(data)

# Sample usage
df_sample = generate_supplier_data(10)
print(df_sample.head())
