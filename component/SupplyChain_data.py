from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# === Individual Attribute Functions ===
def generate_order_id():
    return str(fake.uuid4())

def generate_product_name():
    return fake.word()

def generate_supplier_name():
    return fake.company()

def generate_order_date():
    return fake.date_this_year().strftime("%Y-%m-%d")

def generate_delivery_date():
    return fake.date_between(start_date='today', end_date='+30d').strftime("%Y-%m-%d")

def generate_quantity():
    return random.randint(1, 1000)

def generate_unit_price():
    return round(random.uniform(5, 500), 2)

def calculate_total_cost(quantity, unit_price):
    return round(quantity * unit_price, 2)

def generate_order_status():
    return random.choice(["Pending", "Shipped", "Delivered", "Cancelled"])

def generate_warehouse_location():
    return fake.city()

def generate_transport_mode():
    return random.choice(["Air", "Sea", "Rail", "Road"])

def generate_tracking_number():
    return fake.bothify(text="??###-####")

def generate_inventory_level():
    return random.randint(0, 10000)

def generate_return_status():
    return random.choice(["No Return", "In Process", "Completed"])

def generate_dispatch_center():
    return fake.city()

def generate_shipping_cost():
    return round(random.uniform(5, 200), 2)

def generate_order_priority():
    return random.choice(["High", "Medium", "Low"])

def generate_supplier_contact():
    return fake.phone_number()

def generate_carrier_name():
    return fake.company()

# === Master Data Generation Function ===
def generate_supply_chain_data(num_records=100):
    data = []
    for _ in range(num_records):
        quantity = generate_quantity()
        unit_price = generate_unit_price()
        total_cost = calculate_total_cost(quantity, unit_price)

        data.append({
            "order_id": generate_order_id(),
            "product_name": generate_product_name(),
            "supplier_name": generate_supplier_name(),
            "order_date": generate_order_date(),
            "delivery_date": generate_delivery_date(),
            "quantity": quantity,
            "unit_price": unit_price,
            "total_cost": total_cost,
            "order_status": generate_order_status(),
            "warehouse_location": generate_warehouse_location(),
            "transport_mode": generate_transport_mode(),
            "tracking_number": generate_tracking_number(),
            "inventory_level": generate_inventory_level(),
            "return_status": generate_return_status(),
            "dispatch_center": generate_dispatch_center(),
            "shipping_cost": generate_shipping_cost(),
            "order_priority": generate_order_priority(),
            "supplier_contact": generate_supplier_contact(),
            "carrier_name": generate_carrier_name(),
        })

    return pd.DataFrame(data)

# === Route to download CSV ===
# @app.route('/download_supply_chain_data')
# def download_supply_chain_data():
#     df = generate_supply_chain_data(500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(
#         output,
#         mimetype='text/csv',
#         as_attachment=True,
#         download_name="supply_chain_data.csv"
#     )

# # === Run the Flask App ===
# if __name__ == '__main__':
#     sample_df = generate_supply_chain_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
