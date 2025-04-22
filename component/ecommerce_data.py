from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# Attribute-specific functions
def generate_order_id():
    return str(fake.uuid4())

def generate_customer_id():
    return str(fake.uuid4())

def generate_product_name():
    return fake.word().capitalize() + " " + fake.word().capitalize()

def generate_category():
    return random.choice(["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Books", "Sports"])

def generate_price():
    return round(random.uniform(5, 9999), 2)

def generate_order_date():
    return fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d")

def generate_shipping_date():
    return fake.date_between(start_date='-30d', end_date='today').strftime("%Y-%m-%d")

def generate_payment_method():
    return random.choice(["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash on Delivery"])

def generate_order_status():
    return random.choice(["Processing", "Shipped", "Delivered", "Cancelled", "Returned"])

def generate_quantity():
    return random.randint(1, 10)

def generate_discount():
    return round(random.uniform(0.0, 50.0), 2)

def generate_shipping_cost():
    return round(random.uniform(0.0, 20.0), 2)

def generate_total_amount():
    return round(random.uniform(10.0, 10000.0), 2)

def generate_customer_name():
    return fake.name()

def generate_customer_email():
    return fake.email()

def generate_delivery_address():
    return fake.address()

def generate_tracking_id():
    return fake.bothify(text='??###-#####')

def generate_review_rating():
    return random.randint(1, 5)

def generate_review_comment():
    return fake.sentence(nb_words=12)

def generate_return_reason():
    return random.choice(["Defective", "Wrong Item", "Size Issue", "Changed Mind", "Other"])

# Dataset generator function
def generate_data(num_records=100):
    data = [{
        "order_id": generate_order_id(),
        "customer_id": generate_customer_id(),
        "product_name": generate_product_name(),
        "category": generate_category(),
        "price": generate_price(),
        "order_date": generate_order_date(),
        "shipping_date": generate_shipping_date(),
        "payment_method": generate_payment_method(),
        "order_status": generate_order_status(),
        "quantity": generate_quantity(),
        "discount": generate_discount(),
        "shipping_cost": generate_shipping_cost(),
        "total_amount": generate_total_amount(),
        "customer_name": generate_customer_name(),
        "customer_email": generate_customer_email(),
        "delivery_address": generate_delivery_address(),
        "tracking_id": generate_tracking_id(),
        "review_rating": generate_review_rating(),
        "review_comment": generate_review_comment(),
        "return_reason": generate_return_reason(),
    } for _ in range(num_records)]

    return pd.DataFrame(data)

# Uncomment if you want to serve the file via Flask
# @app.route('/download_ecommerce_data')
# def download_ecommerce_data():
#     df = generate_data(500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="ecommerce_data.csv")

# Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
