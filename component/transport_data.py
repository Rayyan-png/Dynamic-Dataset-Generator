from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate individual transportation data fields
def generate_transport_id():
    return str(fake.uuid4())

def generate_vehicle_type():
    return random.choice(["Car", "Truck", "Bus", "Motorcycle", "Bicycle", "Train"])

def generate_route_number():
    return fake.bothify(text="R-###")

def generate_departure_city():
    return fake.city()

def generate_arrival_city():
    return fake.city()

def generate_departure_time():
    return fake.date_time_this_year()

def generate_arrival_time(departure_time):
    return fake.date_time_between(start_date=departure_time, end_date="+3d")

def generate_ticket_price():
    return round(random.uniform(5, 500), 2)

def generate_driver_name():
    return fake.name()

def generate_passenger_count():
    return random.randint(1, 200)

def generate_transport_status():
    return random.choice(["On Time", "Delayed", "Cancelled"])

def generate_fuel_type():
    return random.choice(["Petrol", "Diesel", "Electric", "Hybrid"])

def generate_license_plate():
    return fake.license_plate()

def generate_transport_company():
    return fake.company()

def generate_cargo_type():
    return random.choice(["General", "Perishable", "Hazardous", "Bulk", "Livestock"])

def generate_vehicle_capacity():
    return random.randint(1000, 50000)  # Capacity in kg

def generate_trip_distance():
    return round(random.uniform(10, 2000), 1)  # Distance in km

def generate_ticket_id():
    return fake.bothify(text="TICKET-####")

def generate_logistics_partner():
    return fake.company()

def generate_inspection_status():
    return random.choice(["Passed", "Failed", "Pending"])

# Function to generate full transportation data
def generate_transportation_data(num_records=100):
    data = []
    for _ in range(num_records):
        departure_time = generate_departure_time()
        arrival_time = generate_arrival_time(departure_time)

        data.append({
            "transport_id": generate_transport_id(),
            "vehicle_type": generate_vehicle_type(),
            "route_number": generate_route_number(),
            "departure_city": generate_departure_city(),
            "arrival_city": generate_arrival_city(),
            "departure_time": departure_time.strftime("%Y-%m-%d %H:%M:%S"),
            "arrival_time": arrival_time.strftime("%Y-%m-%d %H:%M:%S"),
            "ticket_price": generate_ticket_price(),
            "driver_name": generate_driver_name(),
            "passenger_count": generate_passenger_count(),
            "transport_status": generate_transport_status(),
            "fuel_type": generate_fuel_type(),
            "license_plate": generate_license_plate(),
            "transport_company": generate_transport_company(),
            "cargo_type": generate_cargo_type(),
            "vehicle_capacity": generate_vehicle_capacity(),
            "trip_distance": generate_trip_distance(),
            "ticket_id": generate_ticket_id(),
            "logistics_partner": generate_logistics_partner(),
            "inspection_status": generate_inspection_status(),
        })

    return pd.DataFrame(data)

# Flask route to download transportation data as CSV
# @app.route('/download_transportation_data')
# def download_transportation_data():
#     df = generate_transportation_data(5000)  # Generate 5000 records (adjust as needed)

#     # Saving data as CSV file
#     file_path = "transportation_data.csv"
#     df.to_csv(file_path, index=False)

#     return send_file(file_path, as_attachment=True)

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
