from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file
from datetime import datetime

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# ---- Separate functions for each attribute ----
def generate_course_id():
    return str(fake.uuid4())

def generate_course_name():
    return fake.sentence(nb_words=4)

def generate_instructor_name():
    return fake.name()

def generate_student_id():
    return str(fake.uuid4())

def generate_student_name():
    return fake.name()

def generate_enrollment_date():
    return fake.date_this_year()

def generate_completion_date(enrollment_date):
    return fake.date_between(start_date=enrollment_date, end_date="today")

def generate_course_duration_weeks():
    return random.randint(4, 52)

def generate_grade():
    return random.choice(["A", "B", "C", "D", "F"])

def generate_course_level():
    return random.choice(["Beginner", "Intermediate", "Advanced"])

def generate_platform():
    return random.choice(["Udemy", "Coursera", "edX", "Skillshare", "LinkedIn Learning"])

def generate_student_age():
    return random.randint(18, 60)

def generate_country():
    return fake.country()

def generate_language():
    return random.choice(["English", "Spanish", "French", "German", "Chinese"])

def generate_certification_awarded():
    return random.choice([True, False])

def generate_feedback_score():
    return round(random.uniform(0.0, 5.0), 2)

def generate_device_used():
    return random.choice(["Laptop", "Desktop", "Tablet", "Smartphone"])

def generate_payment_method():
    return random.choice(["Credit Card", "Debit Card", "PayPal", "Bank Transfer"])


# ---- Main data generation function ----
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        enrollment_date = generate_enrollment_date()
        completion_date = generate_completion_date(enrollment_date)

        record = {
            "course_id": generate_course_id(),
            "course_name": generate_course_name(),
            "instructor_name": generate_instructor_name(),
            "student_id": generate_student_id(),
            "student_name": generate_student_name(),
            "enrollment_date": enrollment_date,
            "completion_date": completion_date,
            "course_duration_weeks": generate_course_duration_weeks(),
            "grade": generate_grade(),
            "course_level": generate_course_level(),
            "platform": generate_platform(),
            "student_age": generate_student_age(),
            "country": generate_country(),
            "language": generate_language(),
            "certification_awarded": generate_certification_awarded(),
            "feedback_score": generate_feedback_score(),
            "device_used": generate_device_used(),
            "payment_method": generate_payment_method()
        }

        data.append(record)

    return pd.DataFrame(data)

# ---- Flask route for download (optional, commented for now) ----
# @app.route('/download_online_learning_data')
# def download_online_learning_data():
#     df = generate_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="online_learning_data.csv")

# ---- Run for testing ----
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
    # app.run(debug=True)  # Uncomment if using Flask route
