from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# Function to generate individual telecommunication data fields
def generate_subscriber_id():
    return str(fake.uuid4())

def generate_phone_number():
    return fake.phone_number()

def generate_plan_type():
    return random.choice(["Prepaid", "Postpaid", "Family", "Business"])

def generate_data_usage_gb():
    return round(random.uniform(0, 100), 2)  # Adjusted realistic data usage

def generate_call_duration_min():
    return round(random.uniform(0, 1000), 1)  # Adjusted realistic call duration

def generate_sms_count():
    return random.randint(0, 500)

def generate_billing_amount():
    return round(random.uniform(0, 500), 2)  # Adjusted realistic billing amount

def generate_service_provider():
    return fake.company()

def generate_country():
    return fake.country()

def generate_city():
    return fake.city()

def generate_connection_type():
    return random.choice(["4G", "5G", "Fiber", "DSL"])

def generate_activation_date():
    return fake.date_this_decade().strftime("%Y-%m-%d")

def generate_payment_status():
    return random.choice(["Paid", "Pending", "Overdue"])

def generate_customer_age():
    return random.randint(18, 85)

def generate_device_type():
    return random.choice(["Smartphone", "Tablet", "Router", "Smartwatch"])

def generate_network_latency_ms():
    return random.randint(10, 500)

def generate_contract_duration_months():
    return random.randint(1, 36)

def generate_ip_address():
    return fake.ipv4()

def generate_customer_satisfaction():
    return random.choice(["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"])

def generate_data_roaming():
    return random.choices([True, False], weights=[20, 80])[0]  # 20% chance of roaming

# Function to generate full telecommunication data
def generate_telecommunication_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "subscriber_id": generate_subscriber_id(),
            "phone_number": generate_phone_number(),
            "plan_type": generate_plan_type(),
            "data_usage_gb": generate_data_usage_gb(),
            "call_duration_min": generate_call_duration_min(),
            "sms_count": generate_sms_count(),
            "billing_amount": generate_billing_amount(),
            "service_provider": generate_service_provider(),
            "country": generate_country(),
            "city": generate_city(),
            "connection_type": generate_connection_type(),
            "activation_date": generate_activation_date(),
            "payment_status": generate_payment_status(),
            "customer_age": generate_customer_age(),
            "device_type": generate_device_type(),
            "network_latency_ms": generate_network_latency_ms(),
            "contract_duration_months": generate_contract_duration_months(),
            "ip_address": generate_ip_address(),
            "customer_satisfaction": generate_customer_satisfaction(),
            "data_roaming": generate_data_roaming()
        })

    return pd.DataFrame(data)

# Flask route to download telecommunication data as CSV
# @app.route('/download_telecommunication_data')
# def download_telecommunication_data():
#     df = generate_telecommunication_data(5000)  # Generate 5000 records (adjust as needed)

#     # Saving data as CSV file
#     file_path = "telecommunication_data.csv"
#     df.to_csv(file_path, index=False)

#     return send_file(file_path, as_attachment=True)

# Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
