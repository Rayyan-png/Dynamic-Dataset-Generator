from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# Function to generate individual traffic accident data fields
def generate_accident_id():
    return str(fake.uuid4())

def generate_accident_date():
    return fake.date_this_decade().strftime("%Y-%m-%d")

def generate_accident_time():
    return fake.time_object().strftime("%H:%M:%S")

def generate_location():
    return fake.address()

def generate_vehicle_type():
    return random.choice(["Car", "Truck", "Motorcycle", "Bicycle", "Bus"])

def generate_driver_age():
    return random.randint(18, 80)

def generate_weather_condition():
    return random.choice(["Clear", "Rainy", "Snowy", "Foggy", "Windy"])

def generate_cause_of_accident():
    return random.choice(["Speeding", "Distracted Driving", "Drunk Driving", "Weather", "Mechanical Failure"])

def generate_injury_severity():
    return random.choice(["None", "Minor", "Moderate", "Severe", "Fatal"])

def generate_number_of_vehicles():
    return random.randint(1, 5)

def generate_number_of_injuries():
    return random.randint(0, 10)

def generate_number_of_fatalities(num_injuries):
    return random.randint(0, num_injuries)

def generate_accident_description():
    return fake.sentence()

def generate_road_type():
    return random.choice(["Highway", "City Road", "Rural Road", "Residential Area"])

def generate_police_report_number():
    return fake.bothify("PR###-#####")

def generate_hit_and_run():
    return fake.boolean()

def generate_alcohol_involved():
    return fake.boolean()

def generate_speed_at_time():
    return random.randint(20, 150)  # Speed in km/h

def generate_damage_estimation():
    return round(random.uniform(100, 50000), 2)  # Damage cost in USD

def generate_tow_required():
    return fake.boolean()

# Function to generate full traffic accident data
def generate_traffic_accident_data(num_records=100):
    data = []
    for _ in range(num_records):
        num_injuries = generate_number_of_injuries()
        num_fatalities = generate_number_of_fatalities(num_injuries)

        data.append({
            "accident_id": generate_accident_id(),
            "accident_date": generate_accident_date(),
            "accident_time": generate_accident_time(),
            "location": generate_location(),
            "vehicle_type": generate_vehicle_type(),
            "driver_age": generate_driver_age(),
            "weather_condition": generate_weather_condition(),
            "cause_of_accident": generate_cause_of_accident(),
            "injury_severity": generate_injury_severity(),
            "number_of_vehicles": generate_number_of_vehicles(),
            "number_of_injuries": num_injuries,
            "number_of_fatalities": num_fatalities,
            "accident_description": generate_accident_description(),
            "road_type": generate_road_type(),
            "police_report_number": generate_police_report_number(),
            "hit_and_run": generate_hit_and_run(),
            "alcohol_involved": generate_alcohol_involved(),
            "speed_at_time": generate_speed_at_time(),
            "damage_estimation": generate_damage_estimation(),
            "tow_required": generate_tow_required(),
        })

    return pd.DataFrame(data)

# Flask route to download traffic accident data as CSV
# @app.route('/download_traffic_accident_data')
# def download_traffic_accident_data():
#     df = generate_traffic_accident_data(5000)  # Generate 5000 records (adjust as needed)

#     # Saving data as CSV file
#     file_path = "traffic_accident_data.csv"
#     df.to_csv(file_path, index=False)

#     return send_file(file_path, as_attachment=True)

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
