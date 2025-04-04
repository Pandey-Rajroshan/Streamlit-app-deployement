import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import joblib
from datetime import datetime

# Load the model using caching for faster performance
@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model("House_price_predictions.keras")
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

model = load_model()
if model is None:
    st.stop()  # Stop the app if model fails to load

# UI Design
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            color: #333;
        }
        .title {
            text-align: center;
            color: #4CAF50;
            font-size: 36px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #666;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.markdown("<h1 class='title'>🏡 House Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Enter the details below to estimate the house price.</p>", unsafe_allow_html=True)

# User Inputs
id = st.number_input("🏷️ ID", min_value=6762810635, max_value=6762831463, value=6762810635)
Date = st.date_input("📅 Select Built Date", min_value=datetime(1900, 1, 1), max_value=datetime(2025, 1, 1))
number_of_bedrooms = st.number_input("🛏️ Bedrooms", min_value=2, max_value=9, value=3)
number_of_bathrooms = st.number_input("🛁 Bathrooms", min_value=1.0, max_value=6.0, value=2.5)
living_area = st.slider("📏 Living Area (sq ft)", min_value=370, max_value=13540)
lot_area = st.slider("🌍 Lot Area (sq ft)", min_value=520, max_value=1074218)
number_of_floors = st.slider("🏢 Floors", min_value=1.0, max_value=3.5, step=0.5)
waterfront_present = st.slider("🌊 Waterfront (0 or 1)", min_value=0, max_value=1, step=1)
number_of_views = st.slider("👀 Views", min_value=0, max_value=5, step=1)
condition_of_the_house = st.slider("🏠 Condition (1-5)", min_value=1, max_value=5, step=1)
grade_of_the_house = st.slider("⭐ Grade (4-13)", min_value=4, max_value=13, step=1)
Area_excl_basement = st.slider("📏 Area (excluding basement)", min_value=370, max_value=9410, value=490)
Area_basement = st.slider("📦 Basement Area", min_value=0, max_value=4820)
Built_Year = st.slider("🗓️ Built Year", min_value=1900, max_value=2015, step=1)
Renovation_Year = st.slider("🔧 Renovation Year", min_value=0, max_value=2025, step=1)
postal_code = st.number_input("📬 Postal Code", min_value=122003, max_value=122072)
Latitude = st.slider("📍 Latitude", min_value=52.3859, max_value=53.0076, step=0.1)
Longitude = st.slider("📍 Longitude", min_value=-114.709, max_value=-113.505, step=0.1)

# Dynamic Age Calculation
house_age = datetime.now().year - Built_Year
st.write(f"🏡 **House Age:** {house_age} years")

# Prepare input data
input_data = np.array([
    id, Date.toordinal(), number_of_bedrooms, number_of_bathrooms, living_area,
    lot_area, number_of_floors, waterfront_present, number_of_views,
    condition_of_the_house, grade_of_the_house, Area_excl_basement,
    Area_basement, Built_Year, Renovation_Year, postal_code, Latitude,
    Longitude
]).reshape(1, -1)

# Predict Button with Progress Bar
if st.button("🔍 Predict Price"):
    with st.spinner("Predicting house price..."):
        try:
            prediction = model.predict(input_data)
            predicted_price = prediction.flatten()[0]
            
            # Display the result
            st.success(f"🏡 **Estimated Price:** ₹{predicted_price:.2f} lakhs")
            
        except Exception as e:
            st.error(f"⚠️ Prediction Error: {e}")
