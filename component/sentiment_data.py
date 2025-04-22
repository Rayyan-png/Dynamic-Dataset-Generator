from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker and Flask
fake = Faker()
# app = Flask(__name__)

# Separate functions for each attribute
def get_text_id():
    return str(fake.uuid4())

def get_text():
    return fake.sentence(nb_words=20)

def get_sentiment():
    return random.choice(["Positive", "Negative", "Neutral"])

def get_sentiment_score():
    return round(random.uniform(0, 1), 2)

def get_language():
    return random.choice(["English", "Spanish", "French", "German", "Chinese"])

def get_source():
    return random.choice(["Social Media", "News", "Product Review", "Customer Feedback", "Survey"])

def get_timestamp():
    return fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")

def get_author():
    return fake.name()

def get_topic():
    return random.choice(["Politics", "Technology", "Health", "Sports", "Entertainment"])

def get_location():
    return fake.city()

def get_emotion():
    return random.choice(["Happy", "Sad", "Angry", "Excited", "Frustrated"])

def get_device_type():
    return random.choice(["Mobile", "Desktop", "Tablet"])

def get_platform():
    return random.choice(["Twitter", "Facebook", "YouTube", "Instagram", "LinkedIn"])

def get_url():
    return fake.url()

def get_keyword():
    return fake.word()

def get_length_of_text():
    return random.randint(50, 500)

def get_category():
    return random.choice(["Positive Review", "Complaint", "Inquiry", "General Feedback"])

def get_language_confidence():
    return round(random.uniform(0, 1), 2)

def get_user_type():
    return random.choice(["Registered", "Guest", "Anonymous"])

# Function to generate sentiment analysis dataset
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "text_id": get_text_id(),
            "text": get_text(),
            "sentiment": get_sentiment(),
            "sentiment_score": get_sentiment_score(),
            "language": get_language(),
            "source": get_source(),
            "timestamp": get_timestamp(),
            "author": get_author(),
            "topic": get_topic(),
            "location": get_location(),
            "emotion": get_emotion(),
            "device_type": get_device_type(),
            "platform": get_platform(),
            "url": get_url(),
            "keyword": get_keyword(),
            "length_of_text": get_length_of_text(),
            "category": get_category(),
            "language_confidence": get_language_confidence(),
            "user_type": get_user_type()
        })
    return pd.DataFrame(data)

# Flask route to download dataset
# @app.route('/download_sentiment_data')
# def download_sentiment_data():
#     df = generate_data(1000)  # You can change the number here as needed

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="sentiment_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
