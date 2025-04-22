from faker import Faker
import pandas as pd
# from flask import Flask, send_file

fake = Faker()
# app = Flask(__name__)

# Attribute functions
def get_purchase_order_id():
    return fake.uuid4()

def get_supplier_name():
    return fake.company()

def get_product_name():
    return fake.word()

def get_quantity():
    return fake.random_int(min=1, max=500)

def get_unit_price():
    return round(fake.random_number(digits=3) + fake.random_number(digits=2) / 100, 2)

def get_total_cost():
    return round(fake.random_number(digits=4) + fake.random_number(digits=2) / 100, 2)

def get_order_date():
    return fake.date_this_year()

def get_delivery_date():
    return fake.date_between(start_date="today", end_date="+30d")

def get_order_status():
    return fake.random_element(elements=["Pending", "Shipped", "Delivered", "Cancelled"])

def get_payment_status():
    return fake.random_element(elements=["Paid", "Unpaid", "Partially Paid"])

# Main data generation function
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "purchase_order_id": get_purchase_order_id(),
            "supplier_name": get_supplier_name(),
            "product_name": get_product_name(),
            "quantity": get_quantity(),
            "unit_price": get_unit_price(),
            "total_cost": get_total_cost(),
            "order_date": get_order_date(),
            "delivery_date": get_delivery_date(),
            "order_status": get_order_status(),
            "payment_status": get_payment_status(),
        })
    return pd.DataFrame(data)

# Uncomment to enable CSV download via route
# @app.route('/download_purchase_order_data')
# def download_purchase_order_data():
#     df = generate_data(500000)
#     file_path = "purchase_order_data.csv"
#     df.to_csv(file_path, index=False)
#     return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)
