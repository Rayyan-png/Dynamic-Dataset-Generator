from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# Function to generate individual survey data fields
def generate_survey_id():
    return str(fake.uuid4())

def generate_respondent_id():
    return str(fake.uuid4())

def generate_survey_title():
    return fake.sentence(nb_words=5)

def generate_question():
    return fake.sentence(nb_words=10)

def generate_response():
    return random.choice(["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"])

def generate_response_date():
    return fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d")

def generate_location():
    return fake.city()

def generate_age():
    return random.randint(18, 80)

def generate_gender():
    return random.choice(["Male", "Female", "Non-Binary", "Prefer Not to Say"])

def generate_income_level():
    return random.choice(["Low", "Medium", "High"])

def generate_education_level():
    return random.choice(["High School", "Bachelor's", "Master's", "PhD"])

def generate_satisfaction_score():
    return random.randint(1, 10)

def generate_feedback():
    return fake.paragraph(nb_sentences=2)

def generate_device_used():
    return random.choice(["Mobile", "Desktop", "Tablet"])

def generate_channel():
    return random.choice(["Email", "Website", "In-person", "Phone"])

def generate_follow_up_required():
    return random.choices([True, False], weights=[20, 80])[0]  # 20% chance of follow-up

def generate_time_spent():
    return random.randint(1, 60)  # Time in minutes

def generate_ip_address():
    return fake.ipv4()

def generate_language():
    return random.choice(["English", "Spanish", "French", "German", "Chinese"])

def generate_survey_type():
    return random.choice(["Customer Satisfaction", "Market Research", "Employee Feedback", "Product Review"])

# Function to generate full survey data
def generate_survey_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "survey_id": generate_survey_id(),
            "respondent_id": generate_respondent_id(),
            "survey_title": generate_survey_title(),
            "question": generate_question(),
            "response": generate_response(),
            "response_date": generate_response_date(),
            "location": generate_location(),
            "age": generate_age(),
            "gender": generate_gender(),
            "income_level": generate_income_level(),
            "education_level": generate_education_level(),
            "satisfaction_score": generate_satisfaction_score(),
            "feedback": generate_feedback(),
            "device_used": generate_device_used(),
            "channel": generate_channel(),
            "follow_up_required": generate_follow_up_required(),
            "time_spent": generate_time_spent(),
            "ip_address": generate_ip_address(),
            "language": generate_language(),
            "survey_type": generate_survey_type(),
        })

    return pd.DataFrame(data)

# Flask route to download survey data as CSV
# @app.route('/download_survey_data')
# def download_survey_data():
#     df = generate_survey_data(5000)  # Generate 5000 records (adjust as needed)

#     # Saving data as CSV file
#     file_path = "survey_data.csv"
#     df.to_csv(file_path, index=False)

#     return send_file(file_path, as_attachment=True)

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
