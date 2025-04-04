import streamlit as st
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf

st.markdown(
    """
   <style>
   {
   font-family:'sans serif' ,monospace !important; background-color:#FFFFFF; primary-color:#63366;
   text-color:#262730
   }
   <style>
""",
      unsafe_allow_html=True
)
# Load the saved keras model
try:
    model = tf.keras.models.load_model(
        "House_price_predictions.keras")
except Exception as e:
    st.error(f"Error Loading the model: {e}")

# Now you can use model'model.predict()' with user inputs

#Streamlit UI
st.title("Price predictor")
st.write(
    "Enter the following parameters/choices to predict house price")
 
# Collect User inputs
id = st.number_input("ID", min_value=6762810635, max_value=6762831463, value=6762811000)


Date = st.date_input("Select a date")

number_of_bedrooms = st.number_input("number of bedrooms",min_value = 2, max_value = 9 , value = 3 )

number_of_bathrooms = st.number_input("number of bathrooms", min_value=1.0, max_value=6.0, value=2.5)

number_of_bathrooms = st.slider("living area",min_value=370 , max_value=13540)

lot_area = st.slider("select a lot area", min_value=520, max_value=1074218)

number_of_floors = st.slider("number of floors" , min_value= 1.0 , max_value=3.5, step=0.5)

waterfront_present = st.write("number of waterfront present", 0)

number_of_views = st.write("Number of views", 0)

condition_of_the_house = st.slider("condition of the house", min_value=1 , max_value=5, step = 1)

grade_of_the_house = st.slider("Grade Of the house", min_value=4, max_value=13, step = 1)

Area_of_the_house_excluding_basement = st.slider("Area of the house(excluding basement)", min_value=370, max_value=9410 , value = 490)

Area_of_the_basement = st.slider("Area of the basement", min_value= 0 , max_value=4820)

Built_Year = st.slider("Built Year" ,min_value=1900 , max_value=2015 , step = 1)

Renovation_Year = st.write("Renovation Year",0)

postal_code = st.number_input("Enter the postal code" , min_value=122003, max_value=122072)

Lattitude = st.slider("Enter the lattitude" ,  min_value=52.3859 ,max_value=53.0076 ,  step = 0.1)

Longitude = st.slider ("Enter the Longitude", min_value=-114.709 , max_value=-113.505, step=0.1)

living_area_renov = st.slider("Enter the Living Area Renovation", min_value=460, max_value=6110 , step= 10)

lot_area_renov = st.slider("Lot Area Renovation", min_value=651, max_value=560617 , step = 10)

Number_of_schools_nearby = st.slider("Number of schools nearby", min_value=1, max_value=3 , step = 1)

Distance_from_the_Airport = st.slider("Distance from the airport", min_value=50, max_value=80, step=1)


input_data = np.array([
    "id",
    "Date",
    "number_of_bedrooms",
    "number_of_bathrooms",
    "lot_area",
    "number_of_floors",
    "waterfront_present",
    "number_of_views",
    "condition_of_the_house",
    "grade_of_the_house",
    "Area_of_the_house_excluding_basement",
    "Area_of_the_basement",
    "Built_Year",
    "Renovation_Year",
    "postal_code",
    "Lattitude",
    "Longitude",
    "living_area_renov",
    "lot_area_renov",
    "Number_of_schools_nearby",
    "Distance_from_the_Airport"
]).reshape(1,-1)

#Predict the price of the house
if st.button("📊 Predict Price"):
    try:
        prediction = model.predict(input_data)
        
        # Check the type of prediction and process accordingly
        if isinstance(prediction, np.ndarray):
            prediction = float(prediction.flatten()[0])
        elif isinstance(prediction, list):
            prediction = float(prediction[0])
        elif isinstance(prediction, tf.Tensor):
            prediction = float(prediction.numpy().item())
        else:
            raise ValueError("Unexpected data type for prediction.")

        st.success(f"🏡 Estimated Price: ₹{prediction:.2f} lakhs")

    except Exception as e:
        st.error(f"⚠️ Prediction Error: {e}")

