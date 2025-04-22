import os
import importlib

# Get the path to this folder
current_dir = os.path.dirname(__file__)

# Loop through all .py files except __init__.py
for filename in os.listdir(current_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module = importlib.import_module(f"{__name__}.{module_name}")
        globals()[module_name] = module  # Expose as attribute of 'component'


from .agriculture_data import generate_data

from .assets_data import generate_data

from .audio_data import generate_data

from .banking_transaction import generate_transaction_data

from .biometric_data import generate_biometric_data

from .call_center_data import generate_call_center_data

from .copyright_data import generate_copyright_data

from .customer_data import generate_customer_data

from .cybersecurity_data import generate_cybersecurity_data

from .demographics_data import generate_data

from .educational_data import generate_data

from .Energy_consumption_data import generate_data

from .ecommerce_data import generate_data

from .Environmental_data import generate_environmental_data

from .financial_data import generate_data

from .food_supply_chain import generate_food_supply_chain_data

from .gaming_data import generate_gaming_data

from .genomic_data import generate_genomic_data

from .geospatial_data import generate_data

from .governmentsector_data import generate_data

from .HR_data import generate_hr_data

from .image_data import generate_image_data

from .Insurance_data import generate_data

from .Investment_data import generate_investment_data

from .IOT_data import generate_data

from .IT_infrastructure_data import generate_data

from .legal_compliance_data import generate_legal_compliance_data

from .livestock_data import generate_livestock_data

from .logistic_data import generate_data

from .Manufacturing_data import generate_manufacturing_data

from .maritime_data import generate_maritime_data

from .marketing_data import generate_data

from .medical_data import generate_data

from .NLP_data import generate_nlp_data

from .online_learning_data import generate_data

from .pension_data import generate_data

from .real_state_data import generate_data

from .retail_data import generate_retail_data

from .sales_data import generate_data

from .sentiment_data import generate_data

from .social_media_data import generate_data

from .SupplyChain_data import generate_supply_chain_data

from .supports_data import generate_sports_data

from .survey_data import generate_survey_data

from .telecom_data import generate_telecommunication_data

from .Traffic_accident import generate_traffic_accident_data

from .transport_data import generate_transportation_data

from .urban_development import generate_urban_development_data

from .video_data import generate_video_data

from .weather_data import generate_weather_data

from .wildlife_data import generate_wildlife_conservation_data

from .Supplier_data import generate_supplier_data

from .POS_data import generate_data

from .Employee_data import generate_data

from .Order_management_data import generate_data

from .Inventory_data import generate_data

from .billing_invoice_data import generate_invoice_data

from .purchase_order_data import generate_data

from .CRM_data import generate_crm_data

from .user_behaviour import generate_user_behavior_data

from .product_data import generate_data

from .common_fields import generate_data



