from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Individual functions for each attribute
def generate_person_id():
    return str(fake.uuid4())

def generate_first_name():
    return fake.first_name()

def generate_last_name():
    return fake.last_name()

def generate_gender():
    return random.choice(["Male", "Female", "Non-Binary", "Other"])

def generate_age():
    return random.randint(1, 100)

def generate_birth_date():
    return fake.date_of_birth(minimum_age=1, maximum_age=100).strftime("%Y-%m-%d")

def generate_ethnicity():
    return random.choice(["Asian", "Black", "Hispanic", "White", "Mixed", "Other"])

def generate_nationality():
    return fake.country()

def generate_language():
    return fake.language_name()

def generate_education_level():
    return random.choice(["Primary", "Secondary", "High School", "Bachelor's", "Master's", "Doctorate"])

def generate_occupation():
    return fake.job()

def generate_income_level():
    return random.choice(["Low", "Middle", "High"])

def generate_marital_status():
    return random.choice(["Single", "Married", "Divorced", "Widowed"])

def generate_household_size():
    return random.randint(1, 10)

def generate_religion():
    return random.choice(["Christianity", "Islam", "Hinduism", "Buddhism", "Judaism", "None", "Other"])

def generate_residence_type():
    return random.choice(["Urban", "Suburban", "Rural"])

def generate_employment_status():
    return random.choice(["Employed", "Unemployed", "Retired", "Student"])

def generate_health_status():
    return random.choice(["Excellent", "Good", "Fair", "Poor"])

def generate_political_affiliation():
    return random.choice(["Liberal", "Conservative", "Independent", "Other"])

def generate_citizenship_status():
    return random.choice(["Citizen", "Permanent Resident", "Temporary Resident", "Undocumented"])

# Function to generate demographic dataset
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        record = {
            "person_id": generate_person_id(),
            "first_name": generate_first_name(),
            "last_name": generate_last_name(),
            "gender": generate_gender(),
            "age": generate_age(),
            "birth_date": generate_birth_date(),
            "ethnicity": generate_ethnicity(),
            "nationality": generate_nationality(),
            "language": generate_language(),
            "education_level": generate_education_level(),
            "occupation": generate_occupation(),
            "income_level": generate_income_level(),
            "marital_status": generate_marital_status(),
            "household_size": generate_household_size(),
            "religion": generate_religion(),
            "residence_type": generate_residence_type(),
            "employment_status": generate_employment_status(),
            "health_status": generate_health_status(),
            "political_affiliation": generate_political_affiliation(),
            "citizenship_status": generate_citizenship_status(),
        }
        data.append(record)

    return pd.DataFrame(data)

# Optional Flask endpoint (uncomment to use)
# @app.route('/download_demographic_data')
# def download_demographic_data():
#     df = generate_data(500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="demographic_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
