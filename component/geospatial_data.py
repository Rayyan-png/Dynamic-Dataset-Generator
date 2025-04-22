from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Attribute-specific functions
def get_location_id():
    return str(fake.uuid4())

def get_latitude():
    return round(fake.latitude(), 6)

def get_longitude():
    return round(fake.longitude(), 6)

def get_altitude():
    return round(fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=1, max_value=5000), 2)

def get_country():
    return fake.country()

def get_city():
    return fake.city()

def get_zip_code():
    return fake.zipcode()

def get_region():
    return fake.state()

def get_continent():
    return random.choice(["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])

def get_geohash():
    return fake.bothify(text='?????-#####')

def get_address():
    return fake.address()

def get_landmark():
    return fake.street_name()

def get_population_density():
    return fake.random_int(min=1, max=10000)

def get_urban_rural():
    return random.choice(["Urban", "Rural", "Suburban"])

def get_time_zone():
    return fake.timezone()

def get_area_size():
    return round(fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=1, max_value=10000), 2)

def get_climate_zone():
    return random.choice(["Tropical", "Dry", "Temperate", "Continental", "Polar"])

def get_transport_access():
    return random.choice(["Highway", "Railway", "Airport", "Seaport", "None"])

def get_environment_type():
    return random.choice(["Coastal", "Mountainous", "Plains", "Desert", "Forest"])

# Main data generator
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "location_id": get_location_id(),
            "latitude": get_latitude(),
            "longitude": get_longitude(),
            "altitude": get_altitude(),
            "country": get_country(),
            "city": get_city(),
            "zip_code": get_zip_code(),
            "region": get_region(),
            "continent": get_continent(),
            "geohash": get_geohash(),
            "address": get_address(),
            "landmark": get_landmark(),
            "population_density": get_population_density(),
            "urban_rural": get_urban_rural(),
            "time_zone": get_time_zone(),
            "area_size": get_area_size(),
            "climate_zone": get_climate_zone(),
            "transport_access": get_transport_access(),
            "environment_type": get_environment_type(),
        })
    return pd.DataFrame(data)

# Flask route (uncomment to use with API)
# @app.route('/download_geospatial_data')
# def download_geospatial_data():
#     df = generate_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="geospatial_data.csv")

# Test run
if __name__ == '__main__':
    sample_df = generate_data(10)
    print(sample_df.head(10))
    app.run(debug=True)
