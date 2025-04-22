from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# -------- Attribute Generation Functions --------

def get_shipment_id():
    return str(fake.uuid4())

def get_origin():
    return fake.city()

def get_destination():
    return fake.city()

def get_departure_date():
    return fake.date_between(start_date='-1y', end_date='today')

def get_arrival_date(departure_date):
    return fake.date_between(start_date=departure_date, end_date='+1y')

def get_transport_mode():
    return random.choice(["Air", "Sea", "Road", "Rail"])

def get_carrier_name():
    return fake.company()

def get_tracking_number():
    return fake.bothify(text="??-########")

def get_package_weight():
    return round(random.uniform(1.00, 99.99), 2)

def get_package_volume():
    return round(random.uniform(10.00, 999.99), 2)

def get_status():
    return random.choice(["In Transit", "Delivered", "Pending", "Cancelled"])

def get_customer_name():
    return fake.name()

def get_contact_number():
    return fake.phone_number()

def get_shipping_cost():
    return round(random.uniform(100.00, 9999.99), 2)

def get_priority_level():
    return random.choice(["Standard", "Express", "Overnight"])

def get_vehicle_id():
    return fake.bothify(text="???-####")

def get_driver_name():
    return fake.name()

def get_delivery_address():
    return fake.address()

def get_customs_clearance_status():
    return random.choice(["Cleared", "Pending", "Held"])

def get_insurance_coverage():
    return round(random.uniform(1000.00, 99999.99), 2)

# -------- Main Data Generation Function --------

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        departure_date = get_departure_date()
        arrival_date = get_arrival_date(departure_date)

        data.append({
            "shipment_id": get_shipment_id(),
            "origin": get_origin(),
            "destination": get_destination(),
            "departure_date": departure_date.strftime("%Y-%m-%d"),
            "arrival_date": arrival_date.strftime("%Y-%m-%d"),
            "transport_mode": get_transport_mode(),
            "carrier_name": get_carrier_name(),
            "tracking_number": get_tracking_number(),
            "package_weight": get_package_weight(),
            "package_volume": get_package_volume(),
            "status": get_status(),
            "customer_name": get_customer_name(),
            "contact_number": get_contact_number(),
            "shipping_cost": get_shipping_cost(),
            "priority_level": get_priority_level(),
            "vehicle_id": get_vehicle_id(),
            "driver_name": get_driver_name(),
            "delivery_address": get_delivery_address(),
            "customs_clearance_status": get_customs_clearance_status(),
            "insurance_coverage": get_insurance_coverage(),
        })

    return pd.DataFrame(data)

# -------- Optional: CSV Download Route --------
# @app.route('/download_logistics_data')
# def download_logistics_data():
#     df = generate_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="logistics_data.csv")

# -------- Run Flask App Locally --------
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     # app.run(debug=True)
