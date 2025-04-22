from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_call_id():
    return str(fake.uuid4())

def generate_agent_id():
    return fake.random_int(min=100000, max=999999)

def generate_customer_id():
    return str(fake.uuid4())

def generate_call_duration():
    return random.randint(1, 60)  # in minutes

def generate_call_type():
    return random.choice(["Inbound", "Outbound"])

def generate_call_status():
    return random.choice(["Completed", "Missed", "Dropped"])

def generate_call_timestamp():
    return fake.date_time_this_year()

def generate_customer_satisfaction():
    return random.choice(["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"])

def generate_issue_category():
    return random.choice(["Billing", "Technical Support", "General Inquiry", "Complaint"])

def generate_resolution_status():
    return random.choice(["Resolved", "Pending", "Escalated"])

def generate_call_rating():
    return random.randint(1, 5)

def generate_agent_name():
    return fake.name()

def generate_call_center_location():
    return fake.city()

def generate_follow_up_required():
    return random.choice([True, False])

def generate_escalation_level():
    return random.choice(["None", "Level 1", "Level 2", "Level 3"])

def generate_feedback_comments():
    return fake.sentence()

def generate_hold_duration():
    return random.randint(0, 15)  # in minutes

def generate_call_language():
    return random.choice(["English", "Spanish", "French", "German", "Chinese"])

def generate_call_channel():
    return random.choice(["Phone", "Chat", "Email"])

def generate_priority_level():
    return random.choice(["Low", "Medium", "High"])

def generate_call_center_data(num_records=100):
    data = [
        {
            "call_id": generate_call_id(),
            "agent_id": generate_agent_id(),
            "customer_id": generate_customer_id(),
            "call_duration": generate_call_duration(),
            "call_type": generate_call_type(),
            "call_status": generate_call_status(),
            "call_timestamp": generate_call_timestamp(),
            "customer_satisfaction": generate_customer_satisfaction(),
            "issue_category": generate_issue_category(),
            "resolution_status": generate_resolution_status(),
            "call_rating": generate_call_rating(),
            "agent_name": generate_agent_name(),
            "call_center_location": generate_call_center_location(),
            "follow_up_required": generate_follow_up_required(),
            "escalation_level": generate_escalation_level(),
            "feedback_comments": generate_feedback_comments(),
            "hold_duration": generate_hold_duration(),
            "call_language": generate_call_language(),
            "call_channel": generate_call_channel(),
            "priority_level": generate_priority_level()
        } for _ in range(num_records)
    ]
    return pd.DataFrame(data)

# Display sample DataFrame
# df_calls = generate_call_center_data(10)
# print(df_calls.head())
