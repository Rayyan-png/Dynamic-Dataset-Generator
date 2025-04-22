from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# === Attribute Generator Functions ===
def generate_property_id():
    return str(fake.uuid4())

def generate_listing_price():
    return round(random.uniform(50000, 5000000), 2)

def generate_property_type():
    return random.choice(["Apartment", "House", "Condo", "Villa", "Townhouse"])

def generate_address():
    return fake.address()

def generate_city():
    return fake.city()

def generate_state():
    return fake.state()

def generate_zip_code():
    return fake.zipcode()

def generate_country():
    return fake.country()

def generate_bedrooms():
    return random.randint(1, 10)

def generate_bathrooms():
    return random.randint(1, 8)

def generate_square_feet():
    return random.randint(500, 10000)

def generate_listing_date():
    return fake.date_this_year().strftime("%Y-%m-%d")

def generate_sale_status():
    return random.choice(["Available", "Pending", "Sold"])

def generate_agent_name():
    return fake.name()

def generate_agent_phone():
    return fake.phone_number()

def generate_year_built():
    return random.randint(1900, 2023)

def generate_parking_spaces():
    return random.randint(0, 5)

def generate_property_tax():
    return round(random.uniform(1000, 50000), 2)

def generate_listing_description():
    return fake.sentence(nb_words=15)

def generate_hoa_fee():
    return round(random.uniform(50, 5000), 2)

# === Main Data Generation Function ===
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "property_id": generate_property_id(),
            "listing_price": generate_listing_price(),
            "property_type": generate_property_type(),
            "address": generate_address(),
            "city": generate_city(),
            "state": generate_state(),
            "zip_code": generate_zip_code(),
            "country": generate_country(),
            "bedrooms": generate_bedrooms(),
            "bathrooms": generate_bathrooms(),
            "square_feet": generate_square_feet(),
            "listing_date": generate_listing_date(),
            "sale_status": generate_sale_status(),
            "agent_name": generate_agent_name(),
            "agent_phone": generate_agent_phone(),
            "year_built": generate_year_built(),
            "parking_spaces": generate_parking_spaces(),
            "property_tax": generate_property_tax(),
            "listing_description": generate_listing_description(),
            "hoa_fee": generate_hoa_fee(),
        })
    return pd.DataFrame(data)

# === Flask Route to Download CSV ===
# @app.route('/download_real_estate_data')
# def download_real_estate_data():
#     df = generate_data(500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="real_estate_data.csv")

# === Run Flask App ===
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
