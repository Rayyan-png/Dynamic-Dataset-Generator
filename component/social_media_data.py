from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# --- Attribute-specific functions ---

def get_user_id():
    return str(fake.uuid4())

def get_username():
    return fake.user_name()

def get_email():
    return fake.email()

def get_platform():
    return random.choice(["Facebook", "Twitter", "Instagram", "LinkedIn", "TikTok", "Snapchat"])

def get_post_id():
    return str(fake.uuid4())

def get_post_content():
    return fake.sentence(nb_words=20)

def get_post_date():
    return fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")

def get_like_count():
    return random.randint(0, 10000)

def get_comment_count():
    return random.randint(0, 5000)

def get_share_count():
    return random.randint(0, 3000)

def get_followers_count():
    return random.randint(0, 1000000)

def get_following_count():
    return random.randint(0, 5000)

def get_profile_creation_date():
    return fake.date_this_decade().strftime("%Y-%m-%d")

def get_account_status():
    return random.choice(["Active", "Inactive", "Suspended"])

def get_hashtags():
    return ", ".join(fake.words(nb=5))

def get_location():
    return fake.city()

def get_device_type():
    return random.choice(["Mobile", "Desktop", "Tablet"])

def get_engagement_rate():
    return round(random.uniform(0, 1), 4)

def get_content_type():
    return random.choice(["Text", "Image", "Video", "Link"])

def get_ad_impressions():
    return random.randint(0, 100000)

# --- Main data generation function ---

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "user_id": get_user_id(),
            "username": get_username(),
            "email": get_email(),
            "platform": get_platform(),
            "post_id": get_post_id(),
            "post_content": get_post_content(),
            "post_date": get_post_date(),
            "like_count": get_like_count(),
            "comment_count": get_comment_count(),
            "share_count": get_share_count(),
            "followers_count": get_followers_count(),
            "following_count": get_following_count(),
            "profile_creation_date": get_profile_creation_date(),
            "account_status": get_account_status(),
            "hashtags": get_hashtags(),
            "location": get_location(),
            "device_type": get_device_type(),
            "engagement_rate": get_engagement_rate(),
            "content_type": get_content_type(),
            "ad_impressions": get_ad_impressions()
        })
    return pd.DataFrame(data)

# Optional: Flask download route
# @app.route('/download_social_media_data')
# def download_social_media_data():
#     df = generate_data(500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="social_media_data.csv")

# Run for testing
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
