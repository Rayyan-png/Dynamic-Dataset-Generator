from faker import Faker
import pandas as pd
import random
import io
from flask import Flask, send_file

# Initialize Faker & Flask
fake = Faker()
app = Flask(__name__)

# --- Individual Attribute Functions ---

def generate_sample_id():
    return str(fake.uuid4())

def generate_gene_sequence(length=100):
    return ''.join(random.choices("ATCG", k=length))

def generate_gene_name():
    return fake.bothify(text='GENE-###')

def generate_mutation_type():
    return random.choice(["Insertion", "Deletion", "Substitution", "Duplication", "Inversion"])

def generate_chromosome_number():
    return random.randint(1, 23)

def generate_position():
    return random.randint(1000, 1000000)

def generate_genotype():
    return random.choice(["AA", "AT", "TT", "CC", "GG", "AG"])

def generate_expression_level():
    return round(random.uniform(0.001, 99.999), 3)

def generate_variation_frequency():
    return round(random.uniform(0.00001, 1.0), 5)

def generate_disease_association():
    return random.choice(["Cancer", "Diabetes", "Alzheimer's", "Cardiovascular", "None"])

def generate_sample_source():
    return random.choice(["Blood", "Saliva", "Tissue", "Buccal Swab"])

def generate_reference_genome():
    return random.choice(["GRCh37", "GRCh38", "hg19", "hg38"])

def generate_gene_family():
    return random.choice(["Kinase", "Homeobox", "Zinc Finger", "Immunoglobulin"])

def generate_transcription_factor():
    return random.choice(["TP53", "MYC", "SOX2", "PAX6"])

def generate_snp_id():
    return fake.bothify(text='rs#####')

def generate_allele_frequency():
    return round(random.uniform(0.000001, 1.0), 6)

def generate_methylation_level():
    return round(random.uniform(0.01, 100.0), 2)

def generate_exon_number():
    return random.randint(1, 50)

def generate_pathogenicity_score():
    return round(random.uniform(0.0001, 1.0), 4)

# --- Main Generator Function ---
def generate_genomic_data(num_records=100):
    data = []
    for _ in range(num_records):
        data.append({
            "sample_id": generate_sample_id(),
            "gene_sequence": generate_gene_sequence(),
            "gene_name": generate_gene_name(),
            "mutation_type": generate_mutation_type(),
            "chromosome_number": generate_chromosome_number(),
            "position": generate_position(),
            "genotype": generate_genotype(),
            "expression_level": generate_expression_level(),
            "variation_frequency": generate_variation_frequency(),
            "disease_association": generate_disease_association(),
            "sample_source": generate_sample_source(),
            "reference_genome": generate_reference_genome(),
            "gene_family": generate_gene_family(),
            "transcription_factor": generate_transcription_factor(),
            "snp_id": generate_snp_id(),
            "allele_frequency": generate_allele_frequency(),
            "methylation_level": generate_methylation_level(),
            "exon_number": generate_exon_number(),
            "pathogenicity_score": generate_pathogenicity_score(),
        })
    return pd.DataFrame(data)

# --- Flask Route to Download CSV ---
# @app.route('/download_genomic_data')
# def download_genomic_data():
#     df = generate_genomic_data(num_records=1000)  # Change to desired_
