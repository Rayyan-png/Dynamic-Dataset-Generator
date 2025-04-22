from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Attribute-specific functions
def get_ship_id():
    return str(fake.uuid4())

def get_ship_name():
    return fake.company()

def get_port():
    return fake.city()

def get_departure_date():
    return fake.date_between(start_date='-1y', end_date='today')

def get_arrival_date(start_date):
    return fake.date_between(start_date=start_date, end_date='today')

def get_cargo_type():
    return random.choice(["Containers", "Oil", "Gas", "Automobiles", "Electronics", "Food Products"])

def get_ship_type():
    return random.choice(["Cargo", "Tanker", "Cruise", "Fishing", "Naval"])

def get_weight_tons():
    return round(random.uniform(100.00, 100000.00), 2)

def get_crew_size():
    return random.randint(10, 100)

def get_vessel_flag():
    return fake.country_code()

def get_shipping_company():
    return fake.company()

def get_speed_knots():
    return random.randint(10, 40)

def get_navigation_status():
    return random.choice(["Underway", "Anchored", "Moored", "Docked"])

def get_incident_reported():
    return fake.boolean()

def get_registration_number():
    return fake.bothify("SHIP-###-????")

def get_latitude():
    return round(fake.latitude(), 6)

def get_longitude():
    return round(fake.longitude(), 6)

# Function to generate maritime data
def generate_maritime_data(num_records=100):
    data = []
    for _ in range(num_records):
        departure_date = get_departure_date()
        arrival_date = get_arrival_date(departure_date)

        data.append({
            "ship_id": get_ship_id(),
            "ship_name": get_ship_name(),
            "departure_port": get_port(),
            "arrival_port": get_port(),
            "departure_date": departure_date.strftime("%Y-%m-%d"),
            "arrival_date": arrival_date.strftime("%Y-%m-%d"),
            "cargo_type": get_cargo_type(),
            "ship_type": get_ship_type(),
            "weight_tons": get_weight_tons(),
            "crew_size": get_crew_size(),
            "vessel_flag": get_vessel_flag(),
            "shipping_company": get_shipping_company(),
            "speed_knots": get_speed_knots(),
            "navigation_status": get_navigation_status(),
            "incident_reported": get_incident_reported(),
            "ship_registration_number": get_registration_number(),
            "latitude": get_latitude(),
            "longitude": get_longitude(),
        })

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_maritime_data')
# def download_maritime_data():
#     df = generate_maritime_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="maritime_data.csv")

# Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_maritime_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
