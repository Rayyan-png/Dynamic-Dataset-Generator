from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Separate functions for each attribute
def get_citizen_id():
    return str(fake.uuid4())

def get_full_name():
    return fake.name()

def get_birth_date():
    return fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d")

def get_address():
    return fake.address()

def get_city():
    return fake.city()

def get_state():
    return fake.state()

def get_country():
    return fake.country()

def get_postal_code():
    return fake.postcode()

def get_phone_number():
    return fake.phone_number()

def get_email():
    return fake.email()

def get_department():
    return random.choice(["Health", "Education", "Transportation", "Public Safety", "Housing", "Environment"])

def get_service_type():
    return random.choice(["Social Welfare", "Public Works", "Policy Implementation", "Emergency Response", "Community Outreach"])

def get_application_id():
    return fake.bothify(text="APP-###-????")

def get_request_date():
    return fake.date_this_year().strftime("%Y-%m-%d")

def get_processing_status():
    return random.choice(["Pending", "In Progress", "Completed", "Rejected"])

def get_service_fee():
    return round(fake.pydecimal(left_digits=3, right_digits=2, positive=True), 2)

def get_case_officer():
    return fake.name()

def get_service_location():
    return fake.city()

def get_beneficiary_type():
    return random.choice(["Individual", "Organization", "Community Group"])

def get_policy_reference():
    return fake.bothify(text="POL-####-????")

# Data generation function using attribute functions
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "citizen_id": get_citizen_id(),
            "full_name": get_full_name(),
            "birth_date": get_birth_date(),
            "address": get_address(),
            "city": get_city(),
            "state": get_state(),
            "country": get_country(),
            "postal_code": get_postal_code(),
            "phone_number": get_phone_number(),
            "email": get_email(),
            "department": get_department(),
            "service_type": get_service_type(),
            "application_id": get_application_id(),
            "request_date": get_request_date(),
            "processing_status": get_processing_status(),
            "service_fee": get_service_fee(),
            "case_officer": get_case_officer(),
            "service_location": get_service_location(),
            "beneficiary_type": get_beneficiary_type(),
            "policy_reference": get_policy_reference(),
        })

    return pd.DataFrame(data)

# Uncomment this route if you're running it in a Flask app
# @app.route('/download_government_data')
# def download_government_data():
#     df = generate_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="government_data.csv")

# For testing locally
if __name__ == '__main__':
    sample_df = generate_data(10)
    print(sample_df.head(10))
    app.run(debug=True)
