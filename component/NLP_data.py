from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# Attribute Generator Functions
def generate_document_id():
    return str(fake.uuid4())

def generate_text_snippet():
    return fake.text(max_nb_chars=200)

def generate_sentiment():
    return random.choice(["Positive", "Negative", "Neutral"])

def generate_language():
    return random.choice(["English", "Spanish", "French", "German", "Chinese", "Japanese", "Arabic"])

def generate_author():
    return fake.name()

def generate_publication_date():
    return fake.date_between(start_date='-5y', end_date='today')

def generate_topic():
    return random.choice(["Technology", "Health", "Finance", "Education", "Entertainment", "Politics", "Science"])

def generate_text_length():
    return random.randint(50, 10000)

def generate_document_type():
    return random.choice(["Article", "Review", "Report", "Essay", "Blog Post", "Speech", "Transcript"])

def generate_summary():
    return fake.text(max_nb_chars=300)

def generate_keyword():
    return fake.word()

def generate_readability_score():
    return round(random.uniform(0.0, 100.0), 1)

def generate_sentiment_score():
    return round(random.uniform(-1.0, 1.0), 2)

def generate_text_source():
    return random.choice(["News Website", "Social Media", "Journal", "Blog", "Corporate Report"])

def generate_entity_count():
    return random.randint(0, 50)

def generate_named_entities():
    return [fake.company() for _ in range(random.randint(1, 5))]

def generate_emotion():
    return random.choice(["Joy", "Sadness", "Anger", "Surprise", "Fear", "Neutral"])

def generate_language_model():
    return random.choice(["BERT", "GPT", "RoBERTa", "XLNet", "T5"])

def generate_translation():
    return fake.text(max_nb_chars=150)

def generate_source_url():
    return fake.url()

# Main Data Generation Function
def generate_nlp_data(num_records=100):
    data = []
    for _ in range(num_records):
        pub_date = generate_publication_date()
        data.append({
            "document_id": generate_document_id(),
            "text_snippet": generate_text_snippet(),
            "sentiment": generate_sentiment(),
            "language": generate_language(),
            "author": generate_author(),
            "publication_date": pub_date.strftime("%Y-%m-%d"),
            "topic": generate_topic(),
            "text_length": generate_text_length(),
            "document_type": generate_document_type(),
            "summary": generate_summary(),
            "keyword": generate_keyword(),
            "readability_score": generate_readability_score(),
            "sentiment_score": generate_sentiment_score(),
            "text_source": generate_text_source(),
            "entity_count": generate_entity_count(),
            "named_entities": generate_named_entities(),
            "emotion": generate_emotion(),
            "language_model": generate_language_model(),
            "translation": generate_translation(),
            "source_url": generate_source_url()
        })
    return pd.DataFrame(data)

# Flask route to download CSV
# @app.route('/download_nlp_data')
# def download_nlp_data():
#     df = generate_nlp_data(num_records=500000)
#     output = io.BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)
#     return send_file(output, mimetype='text/csv', as_attachment=True, download_name="nlp_data.csv")

# if __name__ == '__main__':
#     sample_df = generate_nlp_data(10)
#     print(sample_df.head(10))
#     app.run(debug=True)
