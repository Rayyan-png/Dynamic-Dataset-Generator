from faker import Faker
import pandas as pd

fake = Faker()

# Attribute generation functions
def generate_employee_id():
    return fake.uuid4()

def generate_name():
    return fake.name()

def generate_age():
    return fake.random_int(min=22, max=65)

def generate_gender():
    return fake.random_element(elements=["Male", "Female", "Non-Binary"])

def generate_department():
    return fake.random_element(elements=["HR", "Finance", "IT", "Marketing", "Sales", "Operations"])

def generate_position():
    return fake.job()

def generate_salary():
    return fake.random_int(min=30000, max=150000)

def generate_hire_date():
    return fake.date_this_decade()

def generate_email():
    return fake.email()

def generate_phone():
    return fake.phone_number()

def generate_address():
    return fake.address()

def generate_employment_status():
    return fake.random_element(elements=["Active", "On Leave", "Resigned", "Terminated"])

# Main data generation function
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "employee_id": generate_employee_id(),
            "name": generate_name(),
            "age": generate_age(),
            "gender": generate_gender(),
            "department": generate_department(),
            "position": generate_position(),
            "salary": generate_salary(),
            "hire_date": generate_hire_date(),
            "email": generate_email(),
            "phone": generate_phone(),
            "address": generate_address(),
            "employment_status": generate_employment_status()
        })
    return pd.DataFrame(data)

# Generate sample data and save to CSV
# df = generate_data(500)
# df.to_csv("employee_data.csv", index=False)
# print("Employee data generated and saved to employee_data.csv")
