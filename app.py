# app.py
# import streamlit as st
# from backend import generate_fake_data, get_faker_mapping

# st.set_page_config(page_title="Dynamic Fake Data Generator", layout="centered")

# st.title("🛠️ Dynamic Fake Data Generator")

# st.markdown("Create a custom dataset by specifying column names and selecting data types from the dropdown.")

# # Number of rows
# num_rows = st.number_input("Number of Rows to Generate", min_value=1, max_value=1000, value=10)

# # Dynamic column input section
# st.subheader("📋 Define Columns")

# data_types = list(get_faker_mapping().keys())

# columns_config = []

# with st.form("column_form"):
#     num_columns = st.number_input("How many columns do you want?", min_value=1, max_value=20, value=3)
#     for i in range(num_columns):
#         col1, col2 = st.columns(2)
#         with col1:
#             col_name = st.text_input(f"Column {i+1} Name", key=f"name_{i}")
#         with col2:
#             col_type = st.selectbox(f"Column {i+1} Data Type", data_types, key=f"type_{i}")
#         columns_config.append({"column_name": col_name, "data_type": col_type})
#     submitted = st.form_submit_button("Generate Data")

# if submitted:
#     if all(col["column_name"] for col in columns_config):
#         df = generate_fake_data(columns_config, num_rows)
#         st.success("✅ Data generated successfully!")
#         st.dataframe(df)

#         # Option to download the data
#         csv = df.to_csv(index=False).encode('utf-8')
#         st.download_button("⬇️ Download CSV", data=csv, file_name="fake_data.csv", mime="text/csv")
#     else:
#         st.error("❗ Please make sure all column names are filled in.")


import streamlit as st
import os
import importlib.util
import pandas as pd
from faker import Faker
from datetime import datetime
from backend import generate_fake_data, get_faker_mapping
import io

# --- Helper Functions ---
def get_dataset_files(folder="D:\\dw project\\component"):
    return [f.replace(".py", "") for f in os.listdir(folder) if f.endswith(".py")]



def generate_fake_data(columns, num_rows):
    fake = Faker()
    mapping = get_faker_mapping()
    data = []
    for _ in range(num_rows):
        row = {}
        for col in columns:
            try:
                row[col["column_name"]] = mapping[col["data_type"]]()
            except:
                row[col["column_name"]] = ""
        data.append(row)
    return pd.DataFrame(data)

# --- UI Layout ---
st.set_page_config(page_title="DataPulse - Professional Dataset Generator", layout="wide")
st.markdown("""
    <style>
        .stTextInput>div>div>input, .stSelectbox>div>div>div {
            border: 1px solid #ccc;
            border-radius: 0.5rem;
        }
        .stButton>button {
            border: 1px solid #4CAF50;
            border-radius: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Pages ---
if "page" not in st.session_state:
    st.session_state.page = "login"

# --- Page: Login ---
if st.session_state.page == "login":
    st.title("🔐 Professional Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:  # Replace with real auth logic
            st.session_state.page = "dataset_selection"
        else:
            st.error("Please enter both username and password.")

# --- Page: Dataset Selection ---
elif st.session_state.page == "dataset_selection":
    st.title("📊 Select Dataset Type")
    dataset_files = get_dataset_files()
    dataset_type = st.selectbox("Choose a dataset type:", dataset_files)
    if st.button("Next ➡️"):
        st.session_state.dataset_type = dataset_type
        st.session_state.page = "define_schema"

# --- Page: Schema Definition ---
elif st.session_state.page == "define_schema":
    st.title("🛠️ Define Schema for " + st.session_state.dataset_type)
    if "table_name" not in st.session_state:
        st.session_state.table_name = ""

    # Input field and save to session_state
    table_name = st.text_input("Define Table Name", value=st.session_state.table_name)
    if table_name:
        st.session_state.table_name = table_name
    table_name = st.session_state.get("table_name", "generated_data")
    



    data_types = list(get_faker_mapping().keys())
    columns_config = []
    with st.form("column_form"):
        num_columns = st.number_input("How many columns do you want?", min_value=1, max_value=20, value=3)
        for i in range(num_columns):
            col1, col2 = st.columns(2)
            with col1:
                col_name = st.text_input(f"Column {i+1} Name", key=f"name_{i}")
            with col2:
                col_type = st.selectbox(f"Column {i+1} Data Type", data_types, key=f"type_{i}")
            columns_config.append({"column_name": col_name, "data_type": col_type})

        submitted = st.form_submit_button("Next ➡️")
        if submitted:
            if all(col["column_name"] for col in columns_config):
                st.session_state.columns_config = columns_config
                st.session_state.page = "record_count"
            else:
                st.error("All column names are required.")

# --- Page: Record Count and Generation ---
elif st.session_state.page == "record_count":
    st.title("📥 Enter Number of Records to Generate")
    num_records = st.number_input("Number of records:", min_value=1, max_value=10000, value=100)
    if st.button("Generate Data 🛠️"):
        df = generate_fake_data(st.session_state.columns_config, num_records)
        st.session_state.generated_data = df
        st.session_state.page = "preview_download"

# --- Page: Preview & Download ---
elif st.session_state.page == "preview_download":
    st.title("📄 Data Preview and Download")
    st.write(st.session_state.generated_data.head())


    col1, col2 = st.columns(2)
    with col1:
        csv = st.session_state.generated_data.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", data=csv, file_name=f"{st.session_state.table_name}.csv", mime="text/csv")

    with col2:
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            st.session_state.generated_data.to_excel(writer, index=False)
        output.seek(0)


# Excel download button
        st.download_button(
            "📥 Download Excel",
            data=output,
            file_name=f"{st.session_state.table_name}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
        # excel = st.session_state.generated_data.to_excel(index=False, engine='openpyxl')
        # st.download_button("📊 Download Excel", data=excel, file_name="generated_data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")



