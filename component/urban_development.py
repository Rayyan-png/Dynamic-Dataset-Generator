from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# Function to generate individual urban development data fields
def generate_project_id():
    return str(fake.uuid4())

def generate_project_name():
    return fake.company() + " Urban Development"

def generate_location():
    return fake.city()

def generate_start_date():
    return fake.date_between(start_date='-10y', end_date='today')

def generate_end_date(start_date):
    return fake.date_between(start_date=start_date, end_date='+5y')

def generate_budget():
    return round(random.uniform(100000, 50000000), 2)

def generate_project_status():
    return random.choice(["Planning", "In Progress", "Completed", "On Hold"])

def generate_project_manager():
    return fake.name()

def generate_contractor():
    return fake.company()

def generate_building_type():
    return random.choice(["Residential", "Commercial", "Industrial", "Mixed-Use"])

def generate_zone():
    return random.choice(["Urban", "Suburban", "Rural"])

def generate_environmental_impact():
    return random.choice(["Low", "Moderate", "High"])

def generate_permits_issued():
    return random.choice([True, False])

def generate_population_served():
    return random.randint(500, 100000)

def generate_green_certification():
    return random.choice(["LEED", "BREEAM", "None"])

def generate_public_transport_access():
    return random.choice(["High", "Medium", "Low"])

def generate_infrastructure_type():
    return random.choice(["Roads", "Parks", "Utilities", "Mixed"])

def generate_funding_source():
    return random.choice(["Government", "Private", "Public-Private Partnership"])

def generate_land_area():
    return round(random.uniform(0.5, 10000), 2)  # Area in acres

def generate_community_involvement():
    return random.choice(["High", "Medium", "Low"])

# Function to generate full urban development data
def generate_urban_development_data(num_records=100):
    data = []
    for _ in range(num_records):
        start_date = generate_start_date()
        end_date = generate_end_date(start_date)

        data.append({
            "project_id": generate_project_id(),
            "project_name": generate_project_name(),
            "location": generate_location(),
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "budget": generate_budget(),
            "project_status": generate_project_status(),
            "project_manager": generate_project_manager(),
            "contractor": generate_contractor(),
            "building_type": generate_building_type(),
            "zone": generate_zone(),
            "environmental_impact": generate_environmental_impact(),
            "permits_issued": generate_permits_issued(),
            "population_served": generate_population_served(),
            "green_certification": generate_green_certification(),
            "public_transport_access": generate_public_transport_access(),
            "infrastructure_type": generate_infrastructure_type(),
            "funding_source": generate_funding_source(),
            "land_area": generate_land_area(),
            "community_involvement": generate_community_involvement()
        })
    
    return pd.DataFrame(data)

# # Flask route to download urban development data as CSV
# @app.route('/download_urban_development_data')
# def download_urban_development_data():
#     df = generate_urban_development_data(5000)  # Generate 5000 records (adjust as needed)

#     # Saving data as CSV file
#     file_path = "urban_development_data.csv"
#     df.to_csv(file_path, index=False)

#     return send_file(file_path, as_attachment=True)

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
