from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# --- Attribute-specific functions ---

def generate_investment_id():
    return str(fake.uuid4())

def generate_investor_name():
    return fake.name()

def generate_investment_type():
    return random.choice(["Stocks", "Bonds", "Real Estate", "Cryptocurrency", "Mutual Funds", "Commodities"])

def generate_investment_amount():
    return round(random.uniform(1000, 10000000), 2)

def generate_currency():
    return fake.currency_code()

def generate_investment_date():
    return fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d")

def generate_maturity_date():
    return fake.date_between(start_date="today", end_date="+10y").strftime("%Y-%m-%d")

def generate_risk_level():
    return random.choice(["Low", "Medium", "High", "Very High"])

def generate_return_rate():
    return round(random.uniform(1, 20), 2)

def generate_broker_name():
    return fake.company()

def generate_investment_status():
    return random.choice(["Active", "Closed", "Pending", "Withdrawn"])

def generate_account_id():
    return fake.bothify("ACCT-####-????")

def generate_portfolio_id():
    return fake.bothify("PORT-####")

def generate_market_sector():
    return random.choice(["Technology", "Healthcare", "Finance", "Energy", "Consumer Goods"])

def generate_dividends():
    return round(random.uniform(0, 50000), 2)

def generate_tax_rate():
    return round(random.uniform(0, 0.5), 2)

def generate_advisor_name():
    return fake.name()

def generate_geographical_region():
    return fake.country()

def generate_transaction_fee():
    return round(random.uniform(0, 5000), 2)

def generate_investment_strategy():
    return random.choice(["Growth", "Income", "Value", "Balanced", "Aggressive"])

# --- Data Generation Function ---

def generate_investment_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "investment_id": generate_investment_id(),
            "investor_name": generate_investor_name(),
            "investment_type": generate_investment_type(),
            "investment_amount": generate_investment_amount(),
            "currency": generate_currency(),
            "investment_date": generate_investment_date(),
            "maturity_date": generate_maturity_date(),
            "risk_level": generate_risk_level(),
            "return_rate": generate_return_rate(),
            "broker_name": generate_broker_name(),
            "investment_status": generate_investment_status(),
            "account_id": generate_account_id(),
            "portfolio_id": generate_portfolio_id(),
            "market_sector": generate_market_sector(),
            "dividends": generate_dividends(),
            "tax_rate": generate_tax_rate(),
            "advisor_name": generate_advisor_name(),
            "geographical_region": generate_geographical_region(),
            "transaction_fee": generate_transaction_fee(),
            "investment_strategy": generate_investment_strategy(),
        })
    return pd.DataFrame(data)

# --- Flask Route for CSV Download ---

# @app.route('/download_investment_data')
# def download_investment_data():
#     df = generate_investment_data(num_records=1000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="investment_data.csv")

# # --- For Debugging/Testing ---
# if __name__ == '__main__':
#     sample_df = generate_investment_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
