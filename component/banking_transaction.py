from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_transaction_id():
    return str(fake.uuid4())

def generate_account_number():
    return fake.iban()

def generate_transaction_date():
    return fake.date_time_this_year()

def generate_amount():
    return round(float(fake.pydecimal(left_digits=6, right_digits=2, positive=True)), 2)

def generate_currency():
    return fake.currency_code()

def generate_transaction_type():
    return random.choice(["Deposit", "Withdrawal", "Transfer", "Payment"])

def generate_account_balance():
    return round(float(fake.pydecimal(left_digits=7, right_digits=2, positive=True)), 2)

def generate_customer_id():
    return str(fake.uuid4())

def generate_branch_code():
    return fake.random_number(digits=5, fix_len=True)

def generate_transaction_status():
    return random.choice(["Completed", "Pending", "Failed"])

def generate_merchant_name():
    return fake.company()

def generate_payment_method():
    return random.choice(["Online", "ATM", "In-Branch", "Mobile"])

def generate_card_number():
    return fake.credit_card_number()

def generate_card_type():
    return fake.credit_card_provider()

def generate_authorization_code():
    return fake.bothify(text='??###-###')

def generate_reference_number():
    return fake.bothify(text='?????-#####')

def generate_customer_name():
    return fake.name()

def generate_customer_email():
    return fake.email()

def generate_fraud_flag():
    return fake.boolean(chance_of_getting_true=5)

def generate_fee_amount():
    return round(float(fake.pydecimal(left_digits=3, right_digits=2, positive=True)), 2)

def generate_exchange_rate():
    return round(random.uniform(0.5, 2.0), 4)

def generate_transaction_data(num_records=100):
    data = [
        {
            "transaction_id": generate_transaction_id(),
            "account_number": generate_account_number(),
            "transaction_date": generate_transaction_date(),
            "amount": generate_amount(),
            "currency": generate_currency(),
            "transaction_type": generate_transaction_type(),
            "account_balance": generate_account_balance(),
            "customer_id": generate_customer_id(),
            "branch_code": generate_branch_code(),
            "transaction_status": generate_transaction_status(),
            "merchant_name": generate_merchant_name(),
            "payment_method": generate_payment_method(),
            "card_number": generate_card_number(),
            "card_type": generate_card_type(),
            "authorization_code": generate_authorization_code(),
            "reference_number": generate_reference_number(),
            "customer_name": generate_customer_name(),
            "customer_email": generate_customer_email(),
            "fraud_flag": generate_fraud_flag(),
            "fee_amount": generate_fee_amount(),
            "exchange_rate": generate_exchange_rate(),
        } for _ in range(num_records)
    ]
    return pd.DataFrame(data)

# Display sample DataFrame
df_transactions = generate_transaction_data(10)
print(df_transactions.head())
    # app.run(debug=True)  # Uncomment if you want to run the Flask app

# Flask app for CSV download
# @app.route('/download_banking_transaction_data')
# def download_banking_transaction_data():
#     df = generate_banking_transaction_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='banking_transaction_data.csv')
