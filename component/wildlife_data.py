from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_species_id():
    return fake.bothify("SP-####")

def generate_species_name():
    return random.choice(["Tiger", "Elephant", "Panda", "Lion", "Rhino", "Gorilla", "Leopard", "Sea Turtle", "Snow Leopard", "Orangutan"])

def generate_habitat():
    return random.choice(["Forest", "Grassland", "Wetland", "Desert", "Mountain", "Marine", "Savannah"])

def generate_conservation_status():
    return random.choice(["Endangered", "Critically Endangered", "Vulnerable", "Near Threatened", "Least Concern"])

def generate_population_estimate():
    return random.randint(10, 10000)

def generate_protected_area():
    return random.choice(["National Park", "Wildlife Sanctuary", "Biosphere Reserve", "Marine Reserve", "Game Reserve"])

def generate_location():
    return f"{fake.city()}, {fake.country()}"

def generate_tracking_id():
    return str(fake.uuid4())

def generate_last_sighting():
    return fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")

def generate_researcher_name():
    return fake.name()

def generate_project_name():
    return fake.catch_phrase()

def generate_funding_source():
    return fake.company()

def generate_monitoring_method():
    return random.choice(["Camera Trap", "GPS Collar", "Direct Observation", "Acoustic Monitoring", "Satellite Imaging"])

def generate_health_status():
    return random.choice(["Healthy", "Injured", "Deceased", "Unknown"])

def generate_species_behavior():
    return random.choice(["Migrating", "Foraging", "Resting", "Breeding", "Hunting"])

def generate_climate_condition():
    return random.choice(["Sunny", "Rainy", "Snowy", "Cloudy", "Stormy"])

def generate_conservation_agency():
    return fake.company()

def generate_protection_level():
    return random.choice(["High", "Medium", "Low"])

def generate_field_station():
    return fake.bothify("FS-##-??")

def generate_wildlife_conservation_data(num_records=100):
    data = [{
        "species_id": generate_species_id(),
        "species_name": generate_species_name(),
        "habitat": generate_habitat(),
        "conservation_status": generate_conservation_status(),
        "population_estimate": generate_population_estimate(),
        "protected_area": generate_protected_area(),
        "location": generate_location(),
        "tracking_id": generate_tracking_id(),
        "last_sighting": generate_last_sighting(),
        "researcher_name": generate_researcher_name(),
        "project_name": generate_project_name(),
        "funding_source": generate_funding_source(),
        "monitoring_method": generate_monitoring_method(),
        "health_status": generate_health_status(),
        "species_behavior": generate_species_behavior(),
        "climate_condition": generate_climate_condition(),
        "conservation_agency": generate_conservation_agency(),
        "protection_level": generate_protection_level(),
        "field_station": generate_field_station(),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Sample run
# if __name__ == "__main__":
#     df = generate_wildlife_conservation_data(10)
#     print(df.head())
