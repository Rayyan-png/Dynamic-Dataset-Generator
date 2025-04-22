from faker import Faker
import pandas as pd
import random

# Initialize Faker instance
fake = Faker()

# Functions to generate individual fields
def generate_station_id():
    return str(fake.uuid4())

def generate_station_name():
    return f"{fake.city()} Weather Station"

def generate_temperature():
    return round(random.uniform(-30, 50), 1)

def generate_humidity():
    return random.randint(10, 100)

def generate_wind_speed():
    return round(random.uniform(0, 50), 1)

def generate_wind_direction():
    return random.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"])

def generate_precipitation():
    return round(random.uniform(0, 300), 1)

def generate_pressure():
    return round(random.uniform(900, 1100), 1)

def generate_visibility():
    return round(random.uniform(0, 50), 1)

def generate_cloud_cover():
    return random.randint(0, 100)

def generate_weather_condition():
    return random.choice(["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy", "Foggy", "Windy"])

def generate_recorded_at():
    return fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")

def generate_uv_index():
    return random.randint(0, 11)

def generate_air_quality_index():
    return random.randint(0, 500)

def generate_dew_point():
    return round(random.uniform(-20, 30), 1)

def generate_solar_radiation():
    return round(random.uniform(0, 1500), 1)

def generate_fog_density():
    return round(random.uniform(0, 1), 2)

def generate_rainfall_probability():
    return random.randint(0, 100)

def generate_snow_depth():
    return round(random.uniform(0, 100), 1)

# Function to generate full weather data
def generate_weather_data(num_records=100):
    data = [{
        "station_id": generate_station_id(),
        "station_name": generate_station_name(),
        "temperature": generate_temperature(),
        "humidity": generate_humidity(),
        "wind_speed": generate_wind_speed(),
        "wind_direction": generate_wind_direction(),
        "precipitation": generate_precipitation(),
        "pressure": generate_pressure(),
        "visibility": generate_visibility(),
        "cloud_cover": generate_cloud_cover(),
        "weather_condition": generate_weather_condition(),
        "recorded_at": generate_recorded_at(),
        "uv_index": generate_uv_index(),
        "air_quality_index": generate_air_quality_index(),
        "dew_point": generate_dew_point(),
        "solar_radiation": generate_solar_radiation(),
        "fog_density": generate_fog_density(),
        "rainfall_probability": generate_rainfall_probability(),
        "snow_depth": generate_snow_depth(),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Sample usage
df = generate_weather_data(10)
print(df.head())  # Display the first 10 records
