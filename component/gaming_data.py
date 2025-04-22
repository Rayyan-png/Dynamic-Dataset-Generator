from faker import Faker
import pandas as pd
import random
import io
# from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
# app = Flask(__name__)

# --- Attribute Functions ---
def generate_game_id():
    return str(fake.uuid4())

def generate_player_id():
    return str(fake.uuid4())

def generate_player_username():
    return fake.user_name()

def generate_game_name():
    return random.choice(["Battle Royale", "Space Quest", "Mystery Mansion", "Zombie Survival"])

def generate_score():
    return random.randint(0, 10000)

def generate_level_reached():
    return random.randint(1, 50)

def generate_play_time():
    return random.randint(5, 600)

def generate_device_type():
    return random.choice(["PC", "Console", "Mobile"])

def generate_region():
    return random.choice(["North America", "Europe", "Asia", "South America", "Australia"])

def generate_in_game_purchases():
    return random.choice([True, False])

def generate_achievement_unlocked():
    return random.choice(["First Blood", "Speed Runner", "Treasure Hunter", "Master Strategist"])

def generate_match_outcome():
    return random.choice(["Win", "Lose", "Draw"])

def generate_team_size():
    return random.randint(1, 10)

def generate_match_duration():
    return random.randint(5, 120)

def generate_game_mode():
    return random.choice(["Solo", "Duo", "Squad"])

def generate_connection_type():
    return random.choice(["Wi-Fi", "Ethernet", "5G"])

def generate_event_participation():
    return random.choice([True, False])

def generate_item_collected():
    return random.choice(["Health Pack", "Rare Sword", "Magic Shield", "Power Boost"])

def generate_chat_messages():
    return fake.sentence()

def generate_friends_count():
    return random.randint(0, 500)

# --- Data Generator ---
def generate_gaming_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "game_id": generate_game_id(),
            "player_id": generate_player_id(),
            "player_username": generate_player_username(),
            "game_name": generate_game_name(),
            "score": generate_score(),
            "level_reached": generate_level_reached(),
            "play_time": generate_play_time(),
            "device_type": generate_device_type(),
            "region": generate_region(),
            "in_game_purchases": generate_in_game_purchases(),
            "achievement_unlocked": generate_achievement_unlocked(),
            "match_outcome": generate_match_outcome(),
            "team_size": generate_team_size(),
            "match_duration": generate_match_duration(),
            "game_mode": generate_game_mode(),
            "connection_type": generate_connection_type(),
            "event_participation": generate_event_participation(),
            "item_collected": generate_item_collected(),
            "chat_messages": generate_chat_messages(),
            "friends_count": generate_friends_count()
        })
    return pd.DataFrame(data)

# --- Flask Route ---
# @app.route('/download_gaming_data')
# def download_gaming_data():
#     df = generate_gaming_data(num_records=500000)

#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="gaming_data.csv")

# # --- Main ---
# if __name__ == '__main__':
#     sample_df = generate_gaming_data(10)
#     print(sample_df.head(10))  # Show sample data
#     app.run(debug=True)

