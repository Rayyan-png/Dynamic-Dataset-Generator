from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_asset_name():
    return random.choice(["Computer", "Vehicle", "Machinery", "Furniture", "Building"])
def generate_asset_value():
    return round(random.uniform(1000.0, 5000000.0), 2)
def generate_depreciation_rate():
    return round(random.uniform(0.01, 50.0), 2)
def generate_current_value():
    return round(random.uniform(1000.0, 5000000.0), 2)
def generate_current_value():
    return random.choice(["Active", "In Maintenance", "Retired", "Disposed"])
def generate_serial_number():
    return fake.bothify("??-####-??")
def generate_asset_category():
    return random.choice(["Electronics", "Vehicles", "Buildings", "Tools", "Furniture"])
def generate_purchase_price():
    return round(random.uniform(1000.0, 5000000.0), 2)
def generate_usage_hours():
    return random.randint(0, 10000)
def generate_asset_condition():
    return random.choice(["New", "Good", "Fair", "Poor"])
def generate_insurance_policy():
    return fake.bothify("POL-####-###")
def generate_insurance_expiration():
    return fake.date_this_decade()



def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "asset_id": str(fake.uuid4()),  # Ensure UUID is a string
            "asset_name": random.choice(["Computer", "Vehicle", "Machinery", "Furniture", "Building"]),
            "purchase_date": fake.date_this_decade(),
            "asset_value": round(random.uniform(1000.0, 5000000.0), 2),  # No pydecimal issues
            "depreciation_rate": round(random.uniform(0.01, 50.0), 2),  # No pyfloat issues
            "current_value": round(random.uniform(1000.0, 5000000.0), 2),  # No pydecimal issues
            "location": fake.city(),
            "current_value": random.choice(["Active", "In Maintenance", "Retired", "Disposed"]),
            "responsible_person": fake.name(),
            "serial_number": fake.bothify("??-####-??"),
            "warranty_expiration": fake.date_this_decade(),
            "asset_category": random.choice(["Electronics", "Vehicles", "Buildings", "Tools", "Furniture"]),
            "supplier": fake.company(),
            "purchase_price": round(random.uniform(1000.0, 5000000.0), 2),  # No pydecimal issues
            "last_maintenance": fake.date_this_year(),
            "next_maintenance": fake.date_this_year(),
            "usage_hours": random.randint(0, 10000),
            "asset_condition": random.choice(["New", "Good", "Fair", "Poor"]),
            "insurance_policy": fake.bothify("POL-####-###"),
            "insurance_expiration": fake.date_this_decade()
        })
    
    return pd.DataFrame(data)

# Example usage:
df = generate_data(10)
print(df.head())
