from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker and Flask
fake = Faker()
# app = Flask(__name__)

# === Attribute-specific Functions ===
def get_compliance_id():
    return str(fake.uuid4())

def get_regulation_name():
    return random.choice(["GDPR", "HIPAA", "CCPA", "SOX", "PCI DSS", "FISMA"])

def get_compliance_status():
    return random.choice(["Compliant", "Non-Compliant", "Pending Review"])

def get_audit_date():
    return fake.date_this_decade().strftime("%Y-%m-%d")

def get_auditor_name():
    return fake.name()

def get_violation_flag():
    return fake.boolean(chance_of_getting_true=20)

def get_fine_amount():
    return round(random.uniform(1000.00, 1000000.00), 2)

def get_policy_version():
    return fake.bothify("v##.##")

def get_department():
    return random.choice(["Finance", "HR", "IT", "Legal", "Operations"])

def get_remediation_status():
    return random.choice(["Completed", "In Progress", "Not Started"])

def get_risk_level():
    return random.choice(["Low", "Medium", "High", "Critical"])

def get_data_type():
    return random.choice(["Personal Data", "Financial Data", "Medical Data", "Intellectual Property"])

def get_review_cycle():
    return random.choice(["Annual", "Bi-Annual", "Quarterly", "Monthly"])

def get_internal_control():
    return fake.bs()

def get_incident_reported():
    return fake.boolean(chance_of_getting_true=15)

def get_third_party_involvement():
    return fake.boolean(chance_of_getting_true=25)

def get_compliance_officer():
    return fake.name()

def get_documentation_status():
    return random.choice(["Complete", "Partial", "Missing"])

def get_penalty_type():
    return random.choice(["Monetary", "Operational", "Reputational"])

def get_compliance_deadline():
    return fake.date_this_year().strftime("%Y-%m-%d")

# === Main Data Generation Function ===
def generate_legal_compliance_data(num_records=100):
    data = []
    for _ in range(num_records):
        record = {
            "compliance_id": get_compliance_id(),
            "regulation_name": get_regulation_name(),
            "compliance_status": get_compliance_status(),
            "audit_date": get_audit_date(),
            "auditor_name": get_auditor_name(),
            "violation_flag": get_violation_flag(),
            "fine_amount": get_fine_amount(),
            "policy_version": get_policy_version(),
            "department": get_department(),
            "remediation_status": get_remediation_status(),
            "risk_level": get_risk_level(),
            "data_type": get_data_type(),
            "review_cycle": get_review_cycle(),
            "internal_control": get_internal_control(),
            "incident_reported": get_incident_reported(),
            "third_party_involvement": get_third_party_involvement(),
            "compliance_officer": get_compliance_officer(),
            "documentation_status": get_documentation_status(),
            "penalty_type": get_penalty_type(),
            "compliance_deadline": get_compliance_deadline(),
        }
        data.append(record)
    return pd.DataFrame(data)

# === Flask Endpoint ===
# @app.route('/download_legal_compliance_data')
# def download_legal_compliance_data():
#     df = generate_legal_compliance_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="legal_compliance_data.csv")

# # === Run for Testing ===
# if __name__ == '__main__':
#     sample_df = generate_legal_compliance_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
