from faker import Faker

# Initialize Faker first
fake = Faker()

# Generator functions
def generate_address():
    return fake.address()

def generate_id():
    return fake.uuid4()

def generate_boolean():
    return fake.boolean()

def generate_city():
    return fake.city()

def generate_company():
    return "ABC"

def generate_company_email():
    return fake.company_email()

def generate_country():
    return fake.country()

def generate_country_code():
    return fake.country_code()  # Fixed typo here

def generate_credit_card_expire():
    return fake.credit_card_expire()

def generate_credit_card_number():
    return fake.credit_card_number()

def generate_credit_card_provider():
    return fake.credit_card_provider()

def generate_currency_code():
    return fake.currency_code()

def generate_date_this_year():
    return fake.date_this_year()

def generate_date_time_this_year():
    return fake.date_time_this_year()

def generate_email():
    return fake.email()

def generate_first_name():
    return fake.first_name()

def generate_iban():
    return fake.iban()

def generate_image_url():
    return fake.image_url()

def generate_ipv4():
    return fake.ipv4()

def generate_job():
    return fake.job()

def generate_language_name():
    return fake.language_name()

def generate_last_name():
    return fake.last_name()

def generate_latitude():
    return fake.latitude()

def generate_license_plate():
    return fake.license_plate()

def generate_longitude():
    return fake.longitude()

def generate_mac_address():
    return fake.mac_address()

def generate_phone_number():
    return fake.phone_number()

def generate_postcode():
    return fake.postcode()

def generate_state():
    return fake.state()

def generate_street_name():
    return fake.street_name()

def generate_time():
    return fake.time()

def generate_timezone():
    return fake.timezone()

def generate_time_object():
    return fake.time_object()

def generate_url():
    return fake.url()

def generate_user_name():
    return fake.user_name()

def generate_uuid4():
    return fake.uuid4()

def generate_word():
    return fake.word()

def generate_zipcode():
    return fake.zipcode()

def generate_text():
    return fake.text()

def generate_date():
    return fake.date()

def generate_name():
    return fake.name()

# Example data dictionary
def generate_data(num_records=100):
    data = {
        "customer_id": generate_id(),
        "address": generate_address(),
        "boolean": generate_boolean(),
        "Date": generate_date(),
        "city": generate_city(),
        "company": generate_company(), 
        "company_email": generate_company_email(),
        "country": generate_country(),
        "country_code": generate_country_code(),
        "credit_card_expire": generate_credit_card_expire(),
        "credit_card_number": generate_credit_card_number(),
        "credit_card_provider": generate_credit_card_provider(),
        "currency_code": generate_currency_code(),
        "date_this_year": generate_date_this_year(),
        "date_time_this_year": generate_date_time_this_year(),
        "email": generate_email(),
        "first_name": generate_first_name(),
        "iban": generate_iban(),
        "image_url": generate_image_url(),
        "ipv4": generate_ipv4(),
        "job": generate_job(),
        "language_name": generate_language_name(),
        "last_name": generate_last_name(),
        "latitude": generate_latitude(),
        "license_plate": generate_license_plate(),
        "longitude": generate_longitude(),
        "mac_address": generate_mac_address(),
        "phone_number": generate_phone_number(),
        "postcode": generate_postcode(),
        "state": generate_state(),
        "street_name": generate_street_name(),
        "time": generate_time(),
        "time_object": generate_time_object(),
        "timezone": generate_timezone(),
        "url": generate_url(),
        "user_name": generate_user_name(),
        "uuid4": generate_uuid4(),
        "word": generate_word(),
        "text": generate_text(),
        "zipcode": generate_zipcode(),
        "name" : generate_name()
    }
