from faker import Faker
import pandas as pd
from flask import Flask, send_file

fake = Faker()

app = Flask(__name__)

# Function to generate individual user behavior data fields
def generate_user_id():
    return fake.uuid4()

def generate_session_id():
    return fake.uuid4()

def generate_page_views():
    return fake.random_int(min=1, max=50)

def generate_clicks():
    return fake.random_int(min=0, max=100)

def generate_time_spent_seconds():
    return fake.random_int(min=10, max=5000)

def generate_bounce_rate():
    return round(fake.random_number(digits=2) / 100, 2)

def generate_device_type():
    return fake.random_element(elements=["Mobile", "Desktop", "Tablet"])

def generate_browser():
    return fake.random_element(elements=["Chrome", "Firefox", "Safari", "Edge", "Opera"])

def generate_location():
    return fake.city()

def generate_session_start():
    return fake.date_time_this_year()

def generate_session_end():
    return fake.date_time_this_year()

def generate_conversion():
    return fake.random_element(elements=["Yes", "No"])

# Function to generate user behavior data
def generate_user_behavior_data(num_records=100):
    data = [{
        "user_id": generate_user_id(),
        "session_id": generate_session_id(),
        "page_views": generate_page_views(),
        "clicks": generate_clicks(),
        "time_spent_seconds": generate_time_spent_seconds(),
        "bounce_rate": generate_bounce_rate(),
        "device_type": generate_device_type(),
        "browser": generate_browser(),
        "location": generate_location(),
        "session_start": generate_session_start(),
        "session_end": generate_session_end(),
        "conversion": generate_conversion(),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# # Flask route to download user behavior data as CSV
# @app.route('/download_user_behavior_data')
# def download_user_behavior_data():
#     df = generate_user_behavior_data(5000)  # Generate 5000 records (adjust as necessary)

#     # Saving data as CSV file
#     file_path = "user_behavior_data.csv"
#     df.to_csv(file_path, index=False)

#     return send_file(file_path, as_attachment=True)

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
