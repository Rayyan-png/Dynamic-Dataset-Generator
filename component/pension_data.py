from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# === Attribute Generator Functions ===

def get_pensioner_name():
    return fake.name()

def get_pension_type():
    return random.choice(["Government Pension", "Private Pension", "Social Security", "Retirement Savings Plan"])

def get_pension_amount():
    return round(random.uniform(10000, 500000), 2)

def get_currency():
    return fake.currency_code()

def get_retirement_date():
    return fake.date_between(start_date="-30y", end_date="today").strftime("%Y-%m-%d")

def get_pension_status():
    return random.choice(["Active", "Inactive", "Suspended", "Terminated"])

def get_contribution_amount():
    return round(random.uniform(5000, 100000), 2)

def get_beneficiary_name():
    return fake.name()

def get_benefit_frequency():
    return random.choice(["Monthly", "Quarterly", "Annually"])

def get_plan_id():
    return fake.bothify("PLAN-####")

def get_insurer_name():
    return fake.company()

def get_payout_amount():
    return round(random.uniform(10000, 500000), 2)

def get_tax_rate():
    return round(random.uniform(0.01, 0.5), 2)

def get_pension_id():
    return str(fake.uuid4())

def get_advisor_name():
    return fake.name()

def get_geographical_region():
    return fake.country()

def get_employer_contribution():
    return round(random.uniform(5000, 100000), 2)

def get_retirement_age():
    return random.randint(55, 70)

def get_withdrawal_date():
    return fake.date_between(start_date="today", end_date="+20y").strftime("%Y-%m-%d")

def get_investment_strategy():
    return random.choice(["Conservative", "Balanced", "Growth", "Aggressive"])

# === Main Data Generation Function ===

def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "pensioner_name": get_pensioner_name(),
            "pension_type": get_pension_type(),
            "pension_amount": get_pension_amount(),
            "currency": get_currency(),
            "retirement_date": get_retirement_date(),
            "pension_status": get_pension_status(),
            "contribution_amount": get_contribution_amount(),
            "beneficiary_name": get_beneficiary_name(),
            "benefit_frequency": get_benefit_frequency(),
            "plan_id": get_plan_id(),
            "insurer_name": get_insurer_name(),
            "payout_amount": get_payout_amount(),
            "tax_rate": get_tax_rate(),
            "pension_id": get_pension_id(),
            "advisor_name": get_advisor_name(),
            "geographical_region": get_geographical_region(),
            "employer_contribution": get_employer_contribution(),
            "retirement_age": get_retirement_age(),
            "withdrawal_date": get_withdrawal_date(),
            "investment_strategy": get_investment_strategy(),
        })
    return pd.DataFrame(data)

# === Flask Route to Download Data as CSV ===

# @app.route('/download_pension_data')
# def download_pension_data():
#     df = generate_data(num_records=1000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="pension_data.csv")

# # === Run the Flask App ===

# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
