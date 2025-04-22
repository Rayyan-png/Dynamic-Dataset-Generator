from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# --- Attribute Generator Functions ---

def get_product_id():
    return str(fake.uuid4())

def get_product_name():
    return f"{fake.word().capitalize()} {fake.word().capitalize()}"

def get_batch_number():
    return fake.bothify(text="BATCH-####")

def get_manufacturing_date():
    return fake.date_between(start_date='-5y', end_date='today')

def get_expiry_date(manufacturing_date):
    return fake.date_between(start_date=manufacturing_date, end_date='+5y')

def get_factory_location():
    return fake.city()

def get_machine_id():
    return fake.bothify(text="M-###")

def get_worker_id():
    return fake.random_int(min=100000, max=999999)

def get_quality_check_status():
    return random.choice(["Passed", "Failed", "Pending"])

def get_material_used():
    return random.choice(["Steel", "Plastic", "Aluminum", "Wood", "Rubber"])

def get_production_cost():
    return round(random.uniform(100.00, 9999.99), 2)

def get_output_quantity():
    return random.randint(100, 10000)

def get_defect_rate():
    return round(random.uniform(0.001, 0.099), 3)

def get_shift():
    return random.choice(["Day", "Night"])

def get_supervisor_name():
    return fake.name()

def get_power_consumption():
    return round(random.uniform(50.00, 500.00), 2)

def get_production_line():
    return fake.bothify(text="Line-##")

def get_storage_condition():
    return random.choice(["Cool", "Dry", "Ambient"])

def get_shipping_status():
    return random.choice(["Ready", "In Transit", "Delayed"])

def get_equipment_used():
    return random.choice(["CNC Machine", "Conveyor Belt", "Injection Molder", "Lathe", "Press"])

# --- Main Data Generation Function ---

def generate_manufacturing_data(num_records=100):
    data = []
    for _ in range(num_records):
        manufacturing_date = get_manufacturing_date()
        expiry_date = get_expiry_date(manufacturing_date)

        data.append({
            "product_id": get_product_id(),
            "product_name": get_product_name(),
            "batch_number": get_batch_number(),
            "manufacturing_date": manufacturing_date.strftime("%Y-%m-%d"),
            "expiry_date": expiry_date.strftime("%Y-%m-%d"),
            "factory_location": get_factory_location(),
            "machine_id": get_machine_id(),
            "worker_id": get_worker_id(),
            "quality_check_status": get_quality_check_status(),
            "material_used": get_material_used(),
            "production_cost": get_production_cost(),
            "output_quantity": get_output_quantity(),
            "defect_rate": get_defect_rate(),
            "shift": get_shift(),
            "supervisor_name": get_supervisor_name(),
            "power_consumption": get_power_consumption(),
            "production_line": get_production_line(),
            "storage_condition": get_storage_condition(),
            "shipping_status": get_shipping_status(),
            "equipment_used": get_equipment_used(),
        })

    return pd.DataFrame(data)

# --- Optional Flask Route for Download ---
# @app.route('/download_manufacturing_data')
# def download_manufacturing_data():
#     df = generate_manufacturing_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="manufacturing_data.csv")

# --- Run App Locally for Debugging ---
# if __name__ == '__main__':
#     sample_df = generate_manufacturing_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
