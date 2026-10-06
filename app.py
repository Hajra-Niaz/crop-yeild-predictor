import streamlit as st
import numpy as np
import joblib as jb

#Import or Load Model
st.set_page_config(page_title="Crop Predictor",page_icon="🌾",layout="centered")
model=jb.load('crop.pkl')
#Make Navigator 
menu=st.sidebar.title("NAVIGATOR ⏯️")
page=st.sidebar.radio("SELECT",["🏠 HOME","📊 PREDICTOR","✔️ PROBLEM STATEMENT","👭 TEAM MEMBERS","🗂️ ABOUT PROJECT"])
#Home Page:
if page=="🏠 HOME":
    st.title("🌾Crop Yield Prediction")
    st.header("**🎯 Related SDG:**")
    st.write("**Zero Hunger**")
    st.write("**Responsible Consumption and Production**")
    st.header("💡Explanation")	
    st.write("•	By predicting crop yield, farmers can plan resources like fertilizer and water more efficiently.")
    st.write("•	It helps reduce food waste and improves food security by ensuring enough crops are grown.")
    st.write("•	This supports sustainable agriculture and better management of natural resources.")
    st.video("WhatsApp Video 2025-11-04 at 15.08.19.mp4")

#Predictor Page:
if page=="📊 PREDICTOR":
    st.title("Predict Next Month Yield ton/hectare")  
    st.image("crop.jpeg",width=800)
    st.header("Input Your Data to Predict")
    rain=st.number_input("Enter Rainfall_mm",min_value=10,max_value=1500,value=50)
    fertilizer=st.number_input("Enter Fertilizer_kg_per_hectare",min_value=10,max_value=500,value=60) 
    temp=st.slider("Enter Temperature_C",min_value=0,max_value=55,value=20)
    soil=st.selectbox("Soil_Type",["Clay","Loamy","Sandy"])
    soil_dic={"Clay":0,"Loamy":1,"Sandy":2}
    soil_encode=soil_dic[soil]
    if st.button("Predict"):
        input_data=np.array([[rain,fertilizer,temp,soil_encode]])
        result=model.predict(input_data)[0]
        chart=rain,result
        st.success(f"**Yield_ton {round(result,2)}per hectare**")
        import pandas as pd
        st.bar_chart(pd.DataFrame({"inputs":["Rainfall","Temprature","Fertilizer"],
                                   "values":[rain,temp,fertilizer]}).set_index("inputs"))
        st.info("Developed By:Hajra Khilji and Zainab Abbasi✨")            
#Problem Stement Page:
if page=="✔️ PROBLEM STATEMENT":
    st.title("Problem Statement:")    
    st.write("Agriculture is one of the most essential sectors supporting human life and economic stability. However, farmers often face challenges in predicting the expected yield of crops due to fluctuating weather conditions, soil characteristics, and fertilizer usage. Accurate yield prediction can help improve decision-making, optimize resources, and enhance productivity.")
    st.header("Objective:")
    st.write("The objective of this project is to build a machine learning model that predicts the crop yield (in kg/acre) based on four key factors:")
    st.write("**•	🌧️Rainfall (mm)**")
    st.write("**•	🌿Fertilizer Used (kg/acre)**")
    st.write("**•	🌡Temperature (°C)**")
    st.write("**•	🌱Soil Type (e.g., Sandy, Clayey, Loamy)**")
    st.header("Problem Definition:")
    st.write("Given the environmental and soil-related parameters as input, the system should predict the expected yield of the crop. This model can assist farmers and agricultural planners in estimating production and making better farming decisions.")
    st.title("**Expected Output:**")
    st.header("Inputs:")
    st.write("o	Rainfall = 140 mm")
    st.write("o	Fertilizer = 75 kg/acre")
    st.write("o	Soil Type = Loamy")
    st.write("Temperature = 29°C")
    st.header("Output:")
    st.write("o	Predicted Crop Yield = 3.30 kg/acre")

# Team Members Page:     
if page=="👭 TEAM MEMBERS":
    st.title("Team Members:")
    col1,col2=st.columns(2)
    with(col1):
        st.header("**Zainab Abbasi**")
        st.header("About:")
        st.write("IT 3rd Year student,who is Passionate to deal with Artificial Intelligence and Machine Learning✨")
    with(col2):
        st.header("**Hajra Khilji**")
        st.header("About:")
        st.write("IT 3rd Year student,who is Passionate to deal with Artificial Intelligence and Machine Learning✨")   
if page=="🗂️ ABOUT PROJECT":
    st.title("Technology Used:")
    st.write("•	Python for programming")
    st.write("•	Pandas & NumPy for data handling")
    st.write("•	Scikit-learn for model building")
    st.write("•	Streamlit for interactive web app deployment")
    st.video("WhatsApp Video 2025-11-04 at 15.21.04.mp4")