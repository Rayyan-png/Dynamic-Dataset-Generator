from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# === Attribute Functions ===
def generate_product_id():
    return str(fake.uuid4())

def generate_product_name():
    return f"{fake.word().title()} {fake.word().title()}"

def generate_supplier():
    return fake.company()

def generate_batch_number():
    return fake.bothify("??-#####")

def generate_production_date():
    return fake.date_this_decade()

def generate_expiration_date(start_date):
    return fake.date_between(start_date=start_date, end_date="+2y")

def generate_quantity():
    return random.randint(10, 1000)

def generate_storage_temperature():
    return round(random.uniform(0, 30), 1)

def generate_transport_method():
    return random.choice(["Truck", "Ship", "Airplane", "Train"])

def generate_origin_country():
    return fake.country()

def generate_destination_country():
    return fake.country()

def generate_quality_check():
    return random.choice([True, False])

def generate_shipping_cost():
    return round(random.uniform(10, 5000), 2)

def generate_delivery_status():
    return random.choice(["Pending", "In Transit", "Delivered", "Delayed"])

def generate_food_category():
    return random.choice(["Dairy", "Meat", "Vegetables", "Fruits", "Grains", "Beverages"])

def generate_packaging_type():
    return random.choice(["Box", "Pallet", "Container", "Bag"])

def generate_barcode():
    return fake.ean13()

def generate_inspection_date():
    return fake.date_this_year()

# === Data Generation Function ===
def generate_food_supply_chain_data(num_records=100):
    data = []
    for _ in range(num_records):
        production_date = generate_production_date()
        expiration_date = generate_expiration_date(production_date)

        data.append({
            "product_id": generate_product_id(),
            "product_name": generate_product_name(),
            "supplier": generate_supplier(),
            "batch_number": generate_batch_number(),
            "production_date": production_date,
            "expiration_date": expiration_date,
            "quantity": generate_quantity(),
            "storage_temperature": generate_storage_temperature(),
            "transport_method": generate_transport_method(),
            "origin_country": generate_origin_country(),
            "destination_country": generate_destination_country(),
            "quality_check": generate_quality_check(),
            "shipping_cost": generate_shipping_cost(),
            "delivery_status": generate_delivery_status(),
            "food_category": generate_food_category(),
            "packaging_type": generate_packaging_type(),
            "barcode": generate_barcode(),
            "inspection_date": generate_inspection_date()
        })

    return pd.DataFrame(data)

# === Optional Flask Route for CSV Download ===
# @app.route('/download_food_supply_chain_data')
# def download_food_supply_chain_data():
#     df = generate_food_supply_chain_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="food_supply_chain_data.csv")

# === Run Flask App for Debugging ===
# if __name__ == '__main__':
#     sample_df = generate_food_supply_chain_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
