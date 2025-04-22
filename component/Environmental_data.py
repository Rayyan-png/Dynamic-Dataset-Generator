from faker import Faker
import pandas as pd
import random
# from flask import Flask, send_file
import io

fake = Faker()
# app = Flask(__name__)

# --- Individual Attribute Functions ---
def get_sensor_id():
    return fake.uuid4()

def get_air_quality_index():
    return random.randint(0, 500)

def get_temperature_celsius():
    return round(random.uniform(-30, 50), 2)

def get_humidity_percent():
    return round(random.uniform(0, 100), 2)

def get_co2_level_ppm():
    return round(random.uniform(300, 5000), 2)

def get_noise_level_db():
    return round(random.uniform(30, 120), 2)

def get_rainfall_mm():
    return round(random.uniform(0, 500), 2)

def get_wind_speed_kph():
    return round(random.uniform(0, 150), 2)

def get_location():
    return fake.city()

def get_country():
    return fake.country()

def get_measurement_date():
    return fake.date_this_decade()

def get_measurement_time():
    return fake.time()

def get_uv_index():
    return round(random.uniform(0, 11), 2)

def get_water_quality_index():
    return random.randint(0, 100)

def get_pm25():
    return round(random.uniform(0, 500), 2)

def get_pm10():
    return round(random.uniform(0, 600), 2)

def get_ozone_level_ppb():
    return round(random.uniform(0, 300), 2)

def get_so2_level_ppb():
    return round(random.uniform(0, 200), 2)

def get_no2_level_ppb():
    return round(random.uniform(0, 400), 2)

def get_pollution_source():
    return fake.random_element(elements=[
        "Vehicle Emissions", "Industrial", "Agricultural", "Natural", "Construction"
    ])

# --- Main Data Generator ---
def generate_environmental_data(num_records=100):
    data = [{
        "sensor_id": get_sensor_id(),
        "air_quality_index": get_air_quality_index(),
        "temperature_celsius": get_temperature_celsius(),
        "humidity_percent": get_humidity_percent(),
        "co2_level_ppm": get_co2_level_ppm(),
        "noise_level_db": get_noise_level_db(),
        "rainfall_mm": get_rainfall_mm(),
        "wind_speed_kph": get_wind_speed_kph(),
        "location": get_location(),
        "country": get_country(),
        "measurement_date": get_measurement_date(),
        "measurement_time": get_measurement_time(),
        "uv_index": get_uv_index(),
        "water_quality_index": get_water_quality_index(),
        "pm25": get_pm25(),
        "pm10": get_pm10(),
        "ozone_level_ppb": get_ozone_level_ppb(),
        "so2_level_ppb": get_so2_level_ppb(),
        "no2_level_ppb": get_no2_level_ppb(),
        "pollution_source": get_pollution_source(),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Optional download route (uncomment to use in a real app)
# @app.route('/download_environmental_data')
# def download_environmental_data():
#     df = generate_environmental_data(500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='environmental_data.csv')

# if __name__ == '__main__':
#     sample_df = generate_environmental_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
