from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Functions to generate individual fields for video data
def generate_video_id():
    return str(fake.uuid4())

def generate_title():
    return fake.sentence(nb_words=6)

def generate_duration():
    return random.randint(10, 14400)  # 10 secs to 4 hours

def generate_resolution():
    return random.choice(["480p", "720p", "1080p", "4K", "8K"])

def generate_format():
    return random.choice(["MP4", "AVI", "MKV", "MOV", "WMV"])

def generate_codec():
    return random.choice(["H.264", "H.265", "VP9", "AV1"])

def generate_bitrate():
    return random.randint(500, 50000)  # Bitrate in kbps

def generate_framerate():
    return random.choice([24, 30, 60, 120])

def generate_aspect_ratio():
    return random.choice(["16:9", "4:3", "21:9", "1:1"])

def generate_file_size():
    return round(random.uniform(50, 100000), 2)  # Size in MB (50MB to 100GB)

def generate_category():
    return random.choice(["Education", "Entertainment", "Sports", "Documentary", "Music", "Gaming"])

def generate_language():
    return random.choice(["English", "Spanish", "French", "Chinese", "Hindi", "Arabic"])

def generate_uploaded_by():
    return fake.name()

def generate_upload_date():
    return fake.date_between(start_date='-5y', end_date='today').strftime("%Y-%m-%d")

def generate_license_type():
    return random.choice(["Creative Commons", "Public Domain", "Standard", "Royalty-Free"])

def generate_audio_codec():
    return random.choice(["AAC", "MP3", "Opus", "FLAC"])

def generate_subtitles():
    return random.choice(["Yes", "No"])

def generate_views():
    return random.randint(0, 10000000)

def generate_likes():
    return random.randint(0, 500000)

def generate_dislikes():
    return random.randint(0, 50000)

# Function to generate video data
def generate_video_data(num_records=100):
    data = [{
        "video_id": generate_video_id(),
        "title": generate_title(),
        "duration": generate_duration(),
        "resolution": generate_resolution(),
        "format": generate_format(),
        "codec": generate_codec(),
        "bitrate": generate_bitrate(),
        "framerate": generate_framerate(),
        "aspect_ratio": generate_aspect_ratio(),
        "file_size": generate_file_size(),
        "category": generate_category(),
        "language": generate_language(),
        "uploaded_by": generate_uploaded_by(),
        "upload_date": generate_upload_date(),
        "license_type": generate_license_type(),
        "audio_codec": generate_audio_codec(),
        "subtitles": generate_subtitles(),
        "views": generate_views(),
        "likes": generate_likes(),
        "dislikes": generate_dislikes(),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_video_data')
# def download_video_data():
#     df = generate_video_data(500000)  # Generate 500,000 records (adjust as necessary)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="video_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_video_data(10)
#     print(sample_df.head(10))  # Display a sample of the generated data
#     app.run(debug=True)
