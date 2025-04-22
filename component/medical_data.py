from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# Separate attribute generators
def generate_patient_id():
    return str(fake.uuid4())

def generate_patient_name():
    return fake.name()

def generate_age():
    return random.randint(0, 100)

def generate_gender():
    return random.choice(["Male", "Female", "Other"])

def generate_diagnosis():
    return random.choice(["Hypertension", "Diabetes", "Asthma", "Flu", "Migraine"])

def generate_admission_date():
    return fake.date_this_decade()

def generate_discharge_date(admission_date):
    return fake.date_between(start_date=admission_date, end_date='today')

def generate_doctor_name():
    return fake.name()

def generate_department():
    return random.choice(["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "General Medicine"])

def generate_medication():
    return random.choice(["Aspirin", "Metformin", "Lisinopril", "Ibuprofen", "Amoxicillin"])

def generate_allergies():
    return random.choice(["None", "Penicillin", "Peanuts", "Shellfish", "Latex"])

def generate_blood_type():
    return random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])

def generate_insurance_provider():
    return fake.company()

def generate_policy_number():
    return fake.bothify("??###-###-####")

def generate_emergency_contact():
    return fake.phone_number()

def generate_visit_type():
    return random.choice(["Inpatient", "Outpatient", "Emergency"])

def generate_procedure():
    return random.choice(["MRI", "CT Scan", "X-Ray", "Blood Test", "Surgery"])

def generate_hospital_name():
    return fake.company()

def generate_billing_amount():
    return round(random.uniform(100.00, 50000.00), 2)

def generate_followup_date():
    return fake.date_between(start_date='today', end_date='+6m')

# Function to generate full medical dataset
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        admission_date = generate_admission_date()
        discharge_date = generate_discharge_date(admission_date)
        followup_date = generate_followup_date()

        data.append({
            "patient_id": generate_patient_id(),
            "patient_name": generate_patient_name(),
            "age": generate_age(),
            "gender": generate_gender(),
            "diagnosis": generate_diagnosis(),
            "admission_date": admission_date.strftime("%Y-%m-%d"),
            "discharge_date": discharge_date.strftime("%Y-%m-%d"),
            "doctor_name": generate_doctor_name(),
            "department": generate_department(),
            "medication": generate_medication(),
            "allergies": generate_allergies(),
            "blood_type": generate_blood_type(),
            "insurance_provider": generate_insurance_provider(),
            "policy_number": generate_policy_number(),
            "emergency_contact": generate_emergency_contact(),
            "visit_type": generate_visit_type(),
            "procedure": generate_procedure(),
            "hospital_name": generate_hospital_name(),
            "billing_amount": generate_billing_amount(),
            "followup_date": followup_date.strftime("%Y-%m-%d"),
        })

    return pd.DataFrame(data)

# Flask route to download the dataset
# @app.route('/download_medical_data')
# def download_medical_data():
#     df = generate_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="medical_data.csv")

# # Run Flask app
# if __name__ == '__main__':
#     sample_df = generate_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
