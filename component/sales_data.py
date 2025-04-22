from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Attribute generation functions
def generate_sale_id():
    return str(fake.uuid4())

def generate_product_name():
    return fake.word().title()

def generate_customer_id():
    return str(fake.uuid4())

def generate_sale_date():
    return fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")

def generate_quantity():
    return random.randint(1, 100)

def generate_unit_price():
    return round(random.uniform(1, 9999), 2)

def generate_total_amount(quantity, unit_price):
    return round(quantity * unit_price, 2)

def generate_discount():
    return round(random.uniform(0, 99), 2)

def generate_payment_method():
    return random.choice(["Credit Card", "Debit Card", "Cash", "Bank Transfer"])

def generate_salesperson():
    return fake.name()

def generate_region():
    return fake.state()

def generate_country():
    return fake.country()

def generate_invoice_number():
    return fake.bothify("INV###-###")

def generate_customer_type():
    return random.choice(["Retail", "Wholesale", "Online"])

def generate_return_status():
    return random.choice(["No Return", "Partial Return", "Full Return"])

def generate_shipping_method():
    return random.choice(["Standard", "Express", "Overnight"])

def generate_delivery_status():
    return random.choice(["Delivered", "Pending", "Cancelled"])

def generate_product_category():
    return random.choice(["Electronics", "Clothing", "Home Appliances", "Books", "Beauty"])

def generate_loyalty_points():
    return random.randint(0, 1000)

def generate_channel():
    return random.choice(["Online", "In-Store", "Phone"])

# Data generation function
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        quantity = generate_quantity()
        unit_price = generate_unit_price()
        total_amount = generate_total_amount(quantity, unit_price)

        record = {
            "sale_id": generate_sale_id(),
            "product_name": generate_product_name(),
            "customer_id": generate_customer_id(),
            "sale_date": generate_sale_date(),
            "quantity": quantity,
            "unit_price": unit_price,
            "total_amount": total_amount,
            "discount": generate_discount(),
            "payment_method": generate_payment_method(),
            "salesperson": generate_salesperson(),
            "region": generate_region(),
            "country": generate_country(),
            "invoice_number": generate_invoice_number(),
            "customer_type": generate_customer_type(),
            "return_status": generate_return_status(),
            "shipping_method": generate_shipping_method(),
            "delivery_status": generate_delivery_status(),
            "product_category": generate_product_category(),
            "loyalty_points": generate_loyalty_points(),
            "channel": generate_channel(),
        }

        data.append(record)
    return pd.DataFrame(data)

# # Flask route to download CSV
# @app.route('/download_sales_data')
# def download_sales_data():
#     df = generate_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="sales_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
