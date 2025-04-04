import streamlit as st
import numpy as np
import tensorflow as tf

# Load the saved Keras model
try:
    model = tf.keras.models.load_model("House_price_predictions.keras")
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()  # Stop the app if the model fails to load

# Streamlit UI
st.title("🏡 House Price Predictor")
st.write("Enter the following parameters to predict the house price")

# User Inputs
id = st.number_input("🏷️ ID", min_value=6762810635, max_value=6762831463, value=6782810735)
Date = st.date_input("📅 Select Built Date")
number_of_bedrooms = st.number_input("🛏️ Number of Bedrooms", min_value=2, max_value=9, value=3)
number_of_bathrooms = st.number_input("🛁 Number of Bathrooms", min_value=1, max_value=6, value=2.5)
living_area = st.slider("📏 Living Area (sq ft)", min_value=370, max_value=13540)
lot_area = st.slider("🌍 Lot Area (sq ft)", min_value=520, max_value=1074218)
number_of_floors = st.slider("🏢 Number of Floors", min_value=1.0, max_value=3.5, step=0.5)
waterfront_present = st.slider("🌊 Waterfront (0 or 1)", min_value=0, max_value=1, step=1)
number_of_views = st.slider("👀 Number of Views", min_value=0, max_value=5, step=1)
condition_of_the_house = st.slider("🏠 Condition of the House", min_value=1, max_value=5, step=1)
grade_of_the_house = st.slider("⭐ Grade of the House", min_value=4, max_value=13, step=1)
Area_of_the_house_excluding_basement = st.slider("📏 Area (Excluding Basement)", min_value=370, max_value=9410, value=490)
Area_of_the_basement = st.slider("📦 Area of the Basement", min_value=0, max_value=4820)
Built_Year = st.slider("🗓️ Built Year", min_value=1900, max_value=2015, step=1)
Renovation_Year = st.slider("🔧 Renovation Year", min_value=0, max_value=2025, step=1)
postal_code = st.number_input("📬 Postal Code", min_value=122003, max_value=122072)
Latitude = st.slider("📍 Latitude", min_value=52.3859, max_value=53.0076, step=0.1)
Longitude = st.slider("📍 Longitude", min_value=-114.709, max_value=-113.505, step=0.1)
living_area_renov = st.slider("🏠 Living Area Renovation", min_value=460, max_value=6110, step=10)
lot_area_renov = st.slider("🌍 Lot Area Renovation", min_value=651, max_value=560617, step=10)
Number_of_schools_nearby = st.slider("🏫 Number of Schools Nearby", min_value=1, max_value=3, step=1)
Distance_from_the_Airport = st.slider("✈️ Distance from the Airport", min_value=50, max_value=80, step=1)

# Prepare input data
input_data = np.array([
    id,
    Date.toordinal(),  # Convert date to numeric format
    number_of_bedrooms,
    number_of_bathrooms,
    living_area,
    lot_area,
    number_of_floors,
    waterfront_present,
    number_of_views,
    condition_of_the_house,
    grade_of_the_house,
    Area_of_the_house_excluding_basement,
    Area_of_the_basement,
    Built_Year,
    Renovation_Year,
    postal_code,
    Latitude,
    Longitude,
    living_area_renov,
    lot_area_renov,
    Number_of_schools_nearby,
    Distance_from_the_Airport
]).reshape(1, -1)

# Predict the price of the house
if st.button("📊 Predict Price"):
    try:
        prediction = model.predict(input_data)
        prediction_value = float(prediction.flatten()[0])  # Ensure prediction is a float
        st.success(f"🏡 Estimated Price: ₹{prediction_value:.2f} lakhs")
    except Exception as e:
        st.error(f"⚠️ Prediction Error: {e}")
