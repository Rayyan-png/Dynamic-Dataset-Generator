from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# ---- Individual attribute generators ----
def generate_animal_id():
    return str(fake.uuid4())

def generate_species():
    return random.choice(["Cattle", "Sheep", "Goat", "Pig", "Chicken", "Horse"])

def generate_breed():
    return fake.word().title() + " Breed"

def generate_birth_date():
    return fake.date_of_birth(minimum_age=0, maximum_age=10).strftime("%Y-%m-%d")

def generate_weight():
    return round(random.uniform(10.00, 1500.00), 2)

def generate_health_status():
    return random.choice(["Healthy", "Sick", "Recovered", "Under Observation"])

def generate_farm_location():
    return f"{fake.city()}, {fake.country()}"

def generate_owner_name():
    return fake.name()

def generate_feed_type():
    return random.choice(["Grass", "Grain", "Silage", "Mixed Feed"])

def generate_checkup_date():
    return fake.date_this_year().strftime("%Y-%m-%d")

def generate_milk_production():
    return round(random.uniform(0.0, 50.0), 1)

def generate_reproductive_status():
    return random.choice(["Pregnant", "Lactating", "Neutered", "Fertile"])

def generate_tag_number():
    return fake.bothify("TAG-###-????")

def generate_vaccination_status():
    return random.choice(["Up-to-date", "Pending", "Overdue"])

def generate_transportation_method():
    return random.choice(["Truck", "Train", "Air", "Ship"])

def generate_destination():
    return f"{fake.city()}, {fake.country()}"

def generate_inspection_result():
    return random.choice(["Passed", "Failed", "Pending"])

def generate_sales_price():
    return round(random.uniform(50.00, 10000.00), 2)

# ---- Livestock data generator ----
def generate_livestock_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "animal_id": generate_animal_id(),
            "species": generate_species(),
            "breed": generate_breed(),
            "birth_date": generate_birth_date(),
            "weight": generate_weight(),
            "health_status": generate_health_status(),
            "farm_location": generate_farm_location(),
            "owner_name": generate_owner_name(),
            "feed_type": generate_feed_type(),
            "veterinary_checkup_date": generate_checkup_date(),
            "milk_production": generate_milk_production(),
            "reproductive_status": generate_reproductive_status(),
            "tag_number": generate_tag_number(),
            "vaccination_status": generate_vaccination_status(),
            "transportation_method": generate_transportation_method(),
            "destination": generate_destination(),
            "inspection_result": generate_inspection_result(),
            "sales_price": generate_sales_price(),
        })
    return pd.DataFrame(data)

# ---- Flask route to download CSV ----
# @app.route('/download_livestock_data')
# def download_livestock_data():
#     df = generate_livestock_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="livestock_data.csv")

# ---- Run app for testing ----
# if __name__ == '__main__':
#     sample_df = generate_livestock_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
