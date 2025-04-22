from faker import Faker
import pandas as pd

fake = Faker()

def generate_invoice_id():
    return str(fake.uuid4())

def generate_customer_id():
    return str(fake.uuid4())

def generate_customer_name():
    return fake.name()

def generate_email():
    return fake.email()

def generate_billing_address():
    return fake.address()

def generate_invoice_date():
    return fake.date_this_year()

def generate_due_date():
    return fake.date_this_year()

def generate_total_amount():
    return round(fake.random_number(digits=5), 2)

def generate_currency():
    return fake.random_element(elements=["USD", "EUR", "GBP", "INR", "AUD"])

def generate_payment_status():
    return fake.random_element(elements=["Paid", "Pending", "Overdue"])

def generate_payment_method():
    return fake.random_element(elements=["Credit Card", "Bank Transfer", "PayPal", "Cash"])

def generate_tax_amount():
    return round(fake.random_number(digits=3), 2)

def generate_discount():
    return round(fake.random_number(digits=2), 2)

def generate_net_amount():
    return round(fake.random_number(digits=5), 2)

def generate_invoice_notes():
    return fake.sentence()

def generate_invoice_data(num_records=100):
    data = [
        {
            "invoice_id": generate_invoice_id(),
            "customer_id": generate_customer_id(),
            "customer_name": generate_customer_name(),
            "email": generate_email(),
            "billing_address": generate_billing_address(),
            "invoice_date": generate_invoice_date(),
            "due_date": generate_due_date(),
            "total_amount": generate_total_amount(),
            "currency": generate_currency(),
            "payment_status": generate_payment_status(),
            "payment_method": generate_payment_method(),
            "tax_amount": generate_tax_amount(),
            "discount": generate_discount(),
            "net_amount": generate_net_amount(),
            "invoice_notes": generate_invoice_notes(),
        } for _ in range(num_records)
    ]
    return pd.DataFrame(data)

# Display sample DataFrame
df_invoices = generate_invoice_data(10)
print(df_invoices.head())
