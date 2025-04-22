from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_incident_id():
    return str(fake.uuid4())

def generate_incident_type():
    return random.choice(["Phishing", "Malware", "Data Breach", "DDoS", "Ransomware"])

def generate_incident_date():
    return fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")

def generate_severity_level():
    return random.choice(["Low", "Medium", "High", "Critical"])

def generate_source_ip():
    return fake.ipv4()

def generate_destination_ip():
    return fake.ipv4()

def generate_attack_vector():
    return random.choice(["Email", "Network", "Application", "Physical Access"])

def generate_compromised_system():
    return random.choice(["Database Server", "Web Server", "User Workstation", "Mobile Device"])

def generate_detection_method():
    return random.choice(["Firewall", "IDS/IPS", "User Report", "SIEM"])

def generate_response_action():
    return random.choice(["Isolated", "Patched", "Monitored", "No Action"])

def generate_affected_department():
    return random.choice(["IT", "Finance", "HR", "Marketing"])

def generate_exfiltrated_data_size():
    return f"{random.randint(1, 100)} MB"

def generate_malware_family():
    return random.choice(["Trojan", "Worm", "Ransomware", "Spyware"])

def generate_patch_status():
    return random.choice(["Patched", "Unpatched", "Pending"])

def generate_reported_by():
    return fake.name()

def generate_incident_duration():
    return f"{random.randint(1, 72)} hours"

def generate_risk_score():
    return round(random.uniform(0, 10), 1)

def generate_attack_motivation():
    return random.choice(["Financial Gain", "Espionage", "Revenge", "Accidental"])

def generate_data_encrypted():
    return random.choice([True, False])

def generate_threat_actor_type():
    return random.choice(["Internal", "External", "Third-party"])

def generate_cybersecurity_data(num_records=100):
    data = [{
        "incident_id": generate_incident_id(),
        "incident_type": generate_incident_type(),
        "incident_date": generate_incident_date(),
        "severity_level": generate_severity_level(),
        "source_ip": generate_source_ip(),
        "destination_ip": generate_destination_ip(),
        "attack_vector": generate_attack_vector(),
        "compromised_system": generate_compromised_system(),
        "detection_method": generate_detection_method(),
        "response_action": generate_response_action(),
        "affected_department": generate_affected_department(),
        "exfiltrated_data_size": generate_exfiltrated_data_size(),
        "malware_family": generate_malware_family(),
        "patch_status": generate_patch_status(),
        "reported_by": generate_reported_by(),
        "incident_duration": generate_incident_duration(),
        "risk_score": generate_risk_score(),
        "attack_motivation": generate_attack_motivation(),
        "data_encrypted": generate_data_encrypted(),
        "threat_actor_type": generate_threat_actor_type(),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Sample usage
df = generate_cybersecurity_data(10)
print(df.head())
