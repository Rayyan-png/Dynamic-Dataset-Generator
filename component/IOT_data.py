from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# ===== Attribute Generators =====
def get_device_id():
    return str(fake.uuid4())

def get_device_type():
    return random.choice(["Sensor", "Smart Light", "Smart Thermostat", "Smart Camera", "Wearable", "Smart Plug"])

def get_temperature():
    return round(random.uniform(-30, 50), 2)

def get_humidity():
    return round(random.uniform(0, 100), 2)

def get_battery_level():
    return random.randint(0, 100)

def get_signal_strength():
    return random.randint(-100, -30)

def get_firmware_version():
    return fake.bothify(text="v?.##")

def get_location():
    return fake.city()

def get_connection_status():
    return random.choice(["Online", "Offline", "Error"])

def get_last_active():
    return fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")

def get_data_rate():
    return round(random.uniform(0.1, 9.9999), 4)

def get_ip_address():
    return fake.ipv4()

def get_mac_address():
    return fake.mac_address()

def get_power_consumption():
    return round(random.uniform(0.01, 99.999), 3)

def get_alert_status():
    return random.choice(["Normal", "Warning", "Critical"])

def get_uptime_hours():
    return random.randint(0, 8760)

def get_device_owner():
    return fake.name()

def get_network_type():
    return random.choice(["WiFi", "Ethernet", "Cellular"])

def get_data_packet_size():
    return random.randint(64, 1500)

def get_device_model():
    return fake.bothify(text="Model-###")

# ===== Main Data Generator =====
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "device_id": get_device_id(),
            "device_type": get_device_type(),
            "temperature": get_temperature(),
            "humidity": get_humidity(),
            "battery_level": get_battery_level(),
            "signal_strength": get_signal_strength(),
            "firmware_version": get_firmware_version(),
            "location": get_location(),
            "connection_status": get_connection_status(),
            "last_active": get_last_active(),
            "data_rate": get_data_rate(),
            "ip_address": get_ip_address(),
            "mac_address": get_mac_address(),
            "power_consumption": get_power_consumption(),
            "alert_status": get_alert_status(),
            "uptime_hours": get_uptime_hours(),
            "device_owner": get_device_owner(),
            "network_type": get_network_type(),
            "data_packet_size": get_data_packet_size(),
            "device_model": get_device_model(),
        })

    return pd.DataFrame(data)

# Flask route to download CSV (optional activation)
# @app.route('/download_iot_data')
# def download_iot_data():
#     df = generate_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="iot_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
