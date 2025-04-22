from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Attribute generation functions
def generate_employee_id():
    return str(fake.uuid4())

def generate_first_name():
    return fake.first_name()

def generate_last_name():
    return fake.last_name()

def generate_department():
    return random.choice(["HR", "IT", "Finance", "Marketing", "Sales", "Operations"])

def generate_position():
    return fake.job()

def generate_hire_date():
    return fake.date_between(start_date='-10y', end_date='today').strftime("%Y-%m-%d")

def generate_salary():
    return round(fake.pyfloat(left_digits=5, right_digits=2, positive=True, min_value=30000, max_value=99999), 2)

def generate_email():
    return fake.company_email()

def generate_phone_number():
    return fake.phone_number()

def generate_performance_rating():
    return random.choice(["Excellent", "Good", "Average", "Below Average", "Poor"])

def generate_employment_status():
    return random.choice(["Active", "On Leave", "Terminated"])

def generate_manager_id():
    return str(fake.uuid4())

def generate_birth_date():
    return fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%Y-%m-%d")

def generate_gender():
    return random.choice(["Male", "Female", "Other"])

def generate_address():
    return fake.address()

def generate_work_location():
    return fake.city()

def generate_contract_type():
    return random.choice(["Full-Time", "Part-Time", "Contract", "Internship"])

def generate_benefit_plan():
    return random.choice(["Basic", "Standard", "Premium", "Executive"])

def generate_leave_balance():
    return random.randint(0, 30)

def generate_promotion_status():
    return random.choice([True, False])

# Data generator using modular functions
def generate_hr_data(num_records=100):
    data = []
    for _ in range(num_records):
        record = {
            "employee_id": generate_employee_id(),
            "first_name": generate_first_name(),
            "last_name": generate_last_name(),
            "department": generate_department(),
            "position": generate_position(),
            "hire_date": generate_hire_date(),
            "salary": generate_salary(),
            "email": generate_email(),
            "phone_number": generate_phone_number(),
            "performance_rating": generate_performance_rating(),
            "employment_status": generate_employment_status(),
            "manager_id": generate_manager_id(),
            "birth_date": generate_birth_date(),
            "gender": generate_gender(),
            "address": generate_address(),
            "work_location": generate_work_location(),
            "contract_type": generate_contract_type(),
            "benefit_plan": generate_benefit_plan(),
            "leave_balance": generate_leave_balance(),
            "promotion_status": generate_promotion_status(),
        }
        data.append(record)

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_hr_data')
# def download_hr_data():
#     df = generate_hr_data(num_records=1000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="hr_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_hr_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
