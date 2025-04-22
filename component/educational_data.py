from faker import Faker
import pandas as pd
import random
# from flask import Flask, send_file
import io

fake = Faker()
# app = Flask(__name__)

# Attribute Generators
def generate_student_id():
    return fake.uuid4()

def generate_student_name():
    return fake.name()

def generate_age():
    return random.randint(18, 30)

def generate_gender():
    return fake.random_element(elements=["Male", "Female", "Non-Binary"])

def generate_course_name():
    return fake.random_element(elements=[
        "Computer Science", "Mathematics", "Physics", "Biology",
        "Economics", "History", "Literature", "Engineering"
    ])

def generate_enrollment_year():
    return random.randint(2015, 2024)

def generate_gpa():
    return round(random.uniform(2.0, 4.0), 2)

def generate_institution_name():
    return fake.company()

def generate_email():
    return fake.email()

def generate_phone_number():
    return fake.phone_number()

def generate_address():
    return fake.address()

def generate_course_code():
    return fake.bothify(text="CSE###")

def generate_credit_hours():
    return random.randint(1, 4)

def generate_semester():
    return fake.random_element(elements=["Spring", "Summer", "Fall", "Winter"])

def generate_faculty_name():
    return fake.name()

def generate_classroom_number():
    return fake.bothify(text="Room ###")

def generate_grade():
    return fake.random_element(elements=["A", "B", "C", "D", "F"])

def generate_scholarship_status():
    return fake.random_element(elements=["Yes", "No"])

def generate_graduation_status():
    return fake.random_element(elements=["Graduated", "In Progress", "Dropped Out"])

def generate_student_club():
    return fake.random_element(elements=[
        "Robotics Club", "Drama Society", "Sports Club", "Music Club", "Debate Club"
    ])

# Data Generation
def generate_data(num_records=100):
    data = [{
        "student_id": generate_student_id(),
        "student_name": generate_student_name(),
        "age": generate_age(),
        "gender": generate_gender(),
        "course_name": generate_course_name(),
        "enrollment_year": generate_enrollment_year(),
        "gpa": generate_gpa(),
        "institution_name": generate_institution_name(),
        "email": generate_email(),
        "phone_number": generate_phone_number(),
        "address": generate_address(),
        "course_code": generate_course_code(),
        "credit_hours": generate_credit_hours(),
        "semester": generate_semester(),
        "faculty_name": generate_faculty_name(),
        "classroom_number": generate_classroom_number(),
        "grade": generate_grade(),
        "scholarship_status": generate_scholarship_status(),
        "graduation_status": generate_graduation_status(),
        "student_club": generate_student_club(),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Uncomment to use in production Flask app
# @app.route('/download_educational_data')
# def download_educational_data():
#     df = generate_data(500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='educational_data.csv')

# For local testing
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
