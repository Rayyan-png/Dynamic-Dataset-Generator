from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker and Flask
fake = Faker()
app = Flask(__name__)

# ------------------ Attribute Generator Functions ------------------ #

def get_campaign_id():
    return str(fake.uuid4())

def get_campaign_name():
    return fake.catch_phrase()

def get_channel():
    return random.choice(["Email", "Social Media", "TV", "Radio", "Online Ads", "Print Media"])

def get_budget():
    return round(random.uniform(1000.00, 10000000.00), 2)

def get_start_date():
    return fake.date_between(start_date='-2y', end_date='-1y')

def get_end_date(start_date):
    return fake.date_between(start_date=start_date, end_date='today')

def get_target_audience():
    return random.choice(["Teenagers", "Adults", "Seniors", "Businesses", "Students"])

def get_conversion_rate():
    return round(random.uniform(0.01, 0.5), 4)

def get_impressions():
    return random.randint(1000, 1000000)

def get_clicks():
    return random.randint(100, 100000)

def get_cost_per_click():
    return round(random.uniform(0.01, 100.00), 2)

def get_roi():
    return round(random.uniform(0.01, 20.00), 2)

def get_region():
    return random.choice(["North America", "Europe", "Asia", "South America", "Africa", "Oceania"])

def get_ad_type():
    return random.choice(["Banner", "Video", "Pop-up", "Native"])

def get_campaign_status():
    return random.choice(["Active", "Completed", "Paused", "Cancelled"])

def get_lead_count():
    return random.randint(10, 10000)

def get_customer_acquisition_cost():
    return round(random.uniform(100.00, 10000.00), 2)

def get_engagement_rate():
    return round(random.uniform(0.01, 0.3), 4)

def get_revenue():
    return round(random.uniform(1000.00, 10000000.00), 2)

def get_feedback():
    return fake.sentence(nb_words=10)

# ------------------ Dataset Generator ------------------ #

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        start_date = get_start_date()
        end_date = get_end_date(start_date)

        data.append({
            "campaign_id": get_campaign_id(),
            "campaign_name": get_campaign_name(),
            "channel": get_channel(),
            "budget": get_budget(),
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "target_audience": get_target_audience(),
            "conversion_rate": get_conversion_rate(),
            "impressions": get_impressions(),
            "clicks": get_clicks(),
            "cost_per_click": get_cost_per_click(),
            "roi": get_roi(),
            "region": get_region(),
            "ad_type": get_ad_type(),
            "campaign_status": get_campaign_status(),
            "lead_count": get_lead_count(),
            "customer_acquisition_cost": get_customer_acquisition_cost(),
            "engagement_rate": get_engagement_rate(),
            "revenue": get_revenue(),
            "feedback": get_feedback(),
        })
    return pd.DataFrame(data)

# ------------------ Flask Route ------------------ #

# @app.route('/download_marketing_data')
# def download_marketing_data():
#     df = generate_data(num_records=5000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="marketing_data.csv")

# # ------------------ Run the App ------------------ #

# if __name__ == '__main__':
#     print(generate_data(10).head(10))
#     app.run(debug=True)
