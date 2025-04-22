from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_user_id():
    return fake.uuid4

def generate_fingerprint_hash():
    return fake.sha256()

def generate_face_id():
    return fake.sha256()

def generate_iris_scan():
    return fake.sha256()

def generate_voice_sample():
    return random.choice(["Male", "Female", "Neutral"])

def generate_hand_geometry():
    return fake.sha256()

def generate_retina_scan():
    return fake.sha256()

def generate_signature_pattern():
    return fake.sha256()

def generate_dna_sequence():
    return fake.sha256()

def generate_gait_pattern():
    return fake.sha256()

def generate_keystroke_dynamics():
    return fake.sha256()

def generate_palm_vein_pattern():
    return fake.sha256()

def generate_ear_shape():
    return random.choice(["Round", "Oval", "Pointed"])

def generate_skin_texture():
    return random.choice(["Smooth", "Rough", "Scarred"])

def generate_facial_landmarks():
    return random.choice(["High Cheekbones", "Wide Jaw", "Pointed Chin"])

def generate_voice_pitch():
    return round(random.uniform(50, 300), 2)  # Hz

def generate_eye_color():
    return random.choice(["Brown", "Blue", "Green", "Hazel", "Gray"])

def generate_body_temperature():
    return round(random.uniform(35, 42), 1)  # °C

def generate_heart_rate():
    return random.randint(60, 100)  # bpm

def generate_blood_pressure():
    return f"{random.randint(90, 140)}/{random.randint(60, 90)}"  # mmHg

def generate_biometric_data(num_records=100):
    data = [
        {
            "user_id": generate_user_id(),
            "fingerprint_hash": generate_fingerprint_hash(),
            "face_id": generate_face_id(),
            "iris_scan": generate_iris_scan(),
            "voice_sample": generate_voice_sample(),
            "hand_geometry": generate_hand_geometry(),
            "retina_scan": generate_retina_scan(),
            "signature_pattern": generate_signature_pattern(),
            "dna_sequence": generate_dna_sequence(),
            "gait_pattern": generate_gait_pattern(),
            "keystroke_dynamics": generate_keystroke_dynamics(),
            "palm_vein_pattern": generate_palm_vein_pattern(),
            "ear_shape": generate_ear_shape(),
            "skin_texture": generate_skin_texture(),
            "facial_landmarks": generate_facial_landmarks(),
            "voice_pitch": generate_voice_pitch(),
            "eye_color": generate_eye_color(),
            "body_temperature": generate_body_temperature(),
            "heart_rate": generate_heart_rate(),
            "blood_pressure": generate_blood_pressure()
        } for _ in range(num_records)
    ]
    return pd.DataFrame(data)

# Display sample DataFrame
df_biometric = generate_biometric_data(10)
print(df_biometric.head())
