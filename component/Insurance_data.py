from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

fake = Faker()
app = Flask(__name__)

# === Attribute Generators ===
def generate_policy_id():
    return str(fake.uuid4())

def generate_policy_holder_name():
    return fake.name()

def generate_policy_type():
    return random.choice(["Health", "Auto", "Home", "Life", "Travel", "Business"])

def generate_premium_amount():
    return round(random.uniform(100, 10000), 2)

def generate_policy_start_date():
    return fake.date_between(start_date='-5y', end_date='today')

def generate_policy_end_date():
    return fake.date_between(start_date='today', end_date='+5y')

def generate_claim_status():
    return random.choice(["Approved", "Pending", "Denied", "In Progress"])

def generate_claim_amount():
    return round(random.uniform(500, 50000), 2)

def generate_insurer_name():
    return fake.company()

def generate_policy_number():
    return fake.bothify(text="??-#####")

def generate_beneficiary_name():
    return fake.name()

def generate_contact_number():
    return fake.phone_number()

def generate_email():
    return fake.email()

def generate_address():
    return fake.address().replace("\n", ", ")

def generate_policy_renewal_status():
    return fake.boolean(chance_of_getting_true=70)

def generate_risk_category():
    return random.choice(["Low", "Medium", "High"])

def generate_policy_discount():
    return round(random.uniform(0, 500), 2)

def generate_underwriter():
    return fake.name()

def generate_claim_date():
    return fake.date_between(start_date='-3y', end_date='today')

def generate_policy_status():
    return random.choice(["Active", "Lapsed", "Cancelled"])


# === Main Data Generator ===
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        start_date = generate_policy_start_date()
        end_date = generate_policy_end_date()
        claim_dt = generate_claim_date()

        data.append({
            "policy_id": generate_policy_id(),
            "policy_holder_name": generate_policy_holder_name(),
            "policy_type": generate_policy_type(),
            "premium_amount": generate_premium_amount(),
            "policy_start_date": start_date.strftime("%Y-%m-%d"),
            "policy_end_date": end_date.strftime("%Y-%m-%d"),
            "claim_status": generate_claim_status(),
            "claim_amount": generate_claim_amount(),
            "insurer_name": generate_insurer_name(),
            "policy_number": generate_policy_number(),
            "beneficiary_name": generate_beneficiary_name(),
            "contact_number": generate_contact_number(),
            "email": generate_email(),
            "address": generate_address(),
            "policy_renewal_status": generate_policy_renewal_status(),
            "risk_category": generate_risk_category(),
            "policy_discount": generate_policy_discount(),
            "underwriter": generate_underwriter(),
            "claim_date": claim_dt.strftime("%Y-%m-%d"),
            "policy_status": generate_policy_status(),
        })

    return pd.DataFrame(data)


# === Optional: Flask Route for CSV Download ===
# @app.route('/download_insurance_data')
# def download_insurance_data():
#     df = generate_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="insurance_data.csv")


# === Run App & Print Sample ===
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
