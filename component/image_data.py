from faker import Faker
import pandas as pd
import random
import io
import json
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# Attribute generators
def generate_image_id():
    return str(fake.uuid4())

def generate_image_url():
    return fake.image_url()

def generate_image_format():
    return random.choice(["JPEG", "PNG", "BMP", "GIF", "TIFF"])

def generate_resolution():
    return f"{random.randint(640, 3840)}x{random.randint(480, 2160)}"

def generate_file_size():
    return f"{random.randint(100, 5000)} KB"

def generate_color_mode():
    return random.choice(["RGB", "CMYK", "Grayscale", "RGBA"])

def generate_capture_device():
    return random.choice(["DSLR", "Smartphone", "Drone", "Webcam", "Security Camera"])

def generate_location():
    return fake.city()

def generate_capture_date():
    date = fake.date_between(start_date='-5y', end_date='today')
    return date.strftime("%Y-%m-%d")

def generate_license_type():
    return random.choice(["Public Domain", "Creative Commons", "Royalty-Free", "Editorial Use Only"])

def generate_alt_text():
    return fake.sentence()

def generate_image_category():
    return random.choice(["Nature", "Urban", "Portrait", "Abstract", "Food", "Sports", "Technology"])

def generate_aspect_ratio():
    return random.choice(["16:9", "4:3", "1:1", "3:2", "21:9"])

def generate_metadata():
    return json.dumps({
        "ISO": random.randint(100, 3200),
        "Aperture": f"f/{random.randint(1, 22)}",
        "Shutter Speed": f"1/{random.randint(30, 8000)}s"
    })

def generate_photographer():
    return fake.name()

def generate_watermark():
    return random.choice([True, False])

def generate_image_tags():
    return json.dumps([fake.word() for _ in range(5)])

def generate_image_source():
    return random.choice(["Stock Library", "User Upload", "Generated", "Archived"])

def generate_focal_length():
    return f"{random.randint(18, 200)}mm"

def generate_image_orientation():
    return random.choice(["Landscape", "Portrait", "Square"])

# Main data generation function
def generate_image_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "image_id": generate_image_id(),
            "image_url": generate_image_url(),
            "image_format": generate_image_format(),
            "resolution": generate_resolution(),
            "file_size": generate_file_size(),
            "color_mode": generate_color_mode(),
            "capture_device": generate_capture_device(),
            "location": generate_location(),
            "capture_date": generate_capture_date(),
            "license_type": generate_license_type(),
            "alt_text": generate_alt_text(),
            "image_category": generate_image_category(),
            "aspect_ratio": generate_aspect_ratio(),
            "metadata": generate_metadata(),
            "photographer": generate_photographer(),
            "watermark": generate_watermark(),
            "image_tags": generate_image_tags(),
            "image_source": generate_image_source(),
            "focal_length": generate_focal_length(),
            "image_orientation": generate_image_orientation(),
        })
    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_image_data')
# def download_image_data():
#     df = generate_image_data(num_records=5000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="image_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_image_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
