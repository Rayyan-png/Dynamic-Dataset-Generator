from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Function to generate individual sports data fields
def generate_match_id():
    return str(fake.uuid4())

def generate_sport_type():
    return random.choice(["Football", "Basketball", "Tennis", "Cricket", "Baseball", "Hockey", "Soccer", "Rugby"])

def generate_team_1():
    return fake.company()

def generate_team_2():
    return fake.company()

def generate_match_date():
    return fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d")

def generate_match_location():
    return fake.city()

def generate_score_team_1():
    return random.randint(0, 10)

def generate_score_team_2():
    return random.randint(0, 10)

def generate_winner(score_team_1, score_team_2):
    if score_team_1 > score_team_2:
        return "Team 1"
    elif score_team_1 < score_team_2:
        return "Team 2"
    else:
        return "Draw"

def generate_referee_name():
    return fake.name()

def generate_duration():
    return random.randint(60, 180)

def generate_tournament_name():
    return fake.catch_phrase()

def generate_player_of_the_match():
    return fake.name()

def generate_attendance():
    return random.randint(1000, 50000)

def generate_ticket_price():
    return round(random.uniform(5, 500), 2)

def generate_weather_conditions():
    return random.choice(["Sunny", "Rainy", "Cloudy", "Windy", "Snowy"])

def generate_broadcast_channel():
    return fake.company()

def generate_sponsor_name():
    return fake.company()

def generate_injury_report():
    return random.choice(["None", "Minor", "Severe"])

def generate_match_status():
    return random.choice(["Completed", "Ongoing", "Scheduled"])

# Function to generate full sports data
def generate_sports_data(num_records=100):
    data = []
    for _ in range(num_records):
        score_team_1 = generate_score_team_1()
        score_team_2 = generate_score_team_2()
        winner = generate_winner(score_team_1, score_team_2)

        data.append({
            "match_id": generate_match_id(),
            "sport_type": generate_sport_type(),
            "team_1": generate_team_1(),
            "team_2": generate_team_2(),
            "match_date": generate_match_date(),
            "match_location": generate_match_location(),
            "score_team_1": score_team_1,
            "score_team_2": score_team_2,
            "winner": winner,
            "referee_name": generate_referee_name(),
            "duration": generate_duration(),
            "tournament_name": generate_tournament_name(),
            "player_of_the_match": generate_player_of_the_match(),
            "attendance": generate_attendance(),
            "ticket_price": generate_ticket_price(),
            "weather_conditions": generate_weather_conditions(),
            "broadcast_channel": generate_broadcast_channel(),
            "sponsor_name": generate_sponsor_name(),
            "injury_report": generate_injury_report(),
            "match_status": generate_match_status(),
        })

    return pd.DataFrame(data)

# Flask route to download sports data as CSV
# @app.route('/download_sports_data')
# def download_sports_data():
#     df = generate_sports_data(5000)  # Generate 5000 records (adjust as needed)

#     # Saving data as CSV file
#     file_path = "sports_data.csv"
#     df.to_csv(file_path, index=False)

#     return send_file(file_path, as_attachment=True)

# # Run Flask app
# if __name__ == '__main__':
#     app.run(debug=True)
