from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# Attribute generation functions
def get_product_id():
    return str(fake.uuid4())

def get_product_name():
    return fake.word().title() + " " + fake.word().title()

def get_category():
    return random.choice(["Electronics", "Clothing", "Home & Garden", "Toys", "Groceries", "Beauty"])

def get_price():
    return round(random.uniform(10, 999), 2)

def get_discount():
    return round(random.uniform(0, 99), 2)

def get_stock_quantity():
    return random.randint(0, 1000)

def get_supplier():
    return fake.company()

def get_brand():
    return fake.company_suffix()

def get_sku():
    return fake.bothify(text='??-#####')

def get_store_location():
    return fake.city()

def get_sale_date():
    return fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d")

def get_customer_id():
    return str(fake.uuid4())

def get_payment_method():
    return random.choice(["Credit Card", "Debit Card", "Cash", "Online Payment"])

def get_return_status():
    return random.choice(["Not Returned", "Returned", "Exchange"])

def get_review_score():
    return random.randint(1, 5)

def get_shipping_cost():
    return round(random.uniform(5, 50), 2)

def get_tax_amount():
    return round(random.uniform(1, 30), 2)

def get_delivery_status():
    return random.choice(["Delivered", "In Transit", "Pending", "Cancelled"])

def get_warranty_period():
    return random.choice(["6 months", "1 year", "2 years", "No Warranty"])

def get_sales_channel():
    return random.choice(["Online", "In-Store", "Wholesale"])

# Function to generate retail data
def generate_retail_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "product_id": get_product_id(),
            "product_name": get_product_name(),
            "category": get_category(),
            "price": get_price(),
            "discount": get_discount(),
            "stock_quantity": get_stock_quantity(),
            "supplier": get_supplier(),
            "brand": get_brand(),
            "sku": get_sku(),
            "store_location": get_store_location(),
            "sale_date": get_sale_date(),
            "customer_id": get_customer_id(),
            "payment_method": get_payment_method(),
            "return_status": get_return_status(),
            "review_score": get_review_score(),
            "shipping_cost": get_shipping_cost(),
            "tax_amount": get_tax_amount(),
            "delivery_status": get_delivery_status(),
            "warranty_period": get_warranty_period(),
            "sales_channel": get_sales_channel(),
        })
    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_retail_data')
# def download_retail_data():
#     df = generate_retail_data(1000)  # adjust as needed

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="retail_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_retail_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
