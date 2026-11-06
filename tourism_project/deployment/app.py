import os
import streamlit as st
import pandas as pd
import joblib

# Load the model committed by the pipeline (sits next to this file)
model_path = os.path.join(os.path.dirname(__file__), "best_tourism_package_modelv1.joblib")
model = joblib.load(model_path)

# Streamlit UI
st.title("Tourism package purchase by customer, predicition")
st.write("""
This application predicts weather a customer purchases the Tourism package base don the information such as
Age, CityTyre, DurationOfPitch,NumberOfPersonVisiting, NumberOfFollowup,PreferredPropertyStar.. etc
please enter the app detail
""")

numeric_features = ["Age", "CityTier", "DurationOfPitch","NumberOfPersonVisiting", "NumberOfFollowups","PreferredPropertyStar",
                    "NumberOfTrips","Passport","PitchSatisfactionScore","OwnCar" ,"NumberOfChildrenVisiting",
                    "MonthlyIncome"]
categorical_features = ["TypeofContact","Occupation","Gender","ProductPitched","MaritalStatus","Designation"]


# User input
TypeofContact_category = st.selectbox("TypeofContact", ["Company Invited", "Self Enquiry"])
Occupation_category = st.selectbox("Occupation", ["Free Lancer", "Large Business", "Salaried","Small Business"])
Gender_category = st.selectbox("Gender", ["Male", "Female"])
ProductPitched_category = st.selectbox("ProductPitched", ["Basic", "Deluxe", "King","Standard","Super Deluxe"])
MaritalStatus_category = st.selectbox("MaritalStatus", ["Married", "Divorced", "Unmarried"])
Designation_category = st.selectbox("Designation", ["VP","AVP","Executive", "Manager", "Senior Manager"])


Age_num = st.number_input("Age", min_value=18, max_value=70, value=18, step=1)
CityTier_num = st.number_input("CityTier", min_value=1, max_value=3, value=1, step=1)
DurationOfPitch_num = st.number_input("DurationOfPitch in mins", min_value=5, max_value=127, value=5, step=1)
NumberOfPersonVisiting_num= st.number_input("NumberOfPersonVisiting", min_value=1, max_value=5, value=1, step=1)
NumberOfFollowups_num = st.number_input("NumberOfFollowups", min_value=1, max_value=6, value=1, step=1)
PreferredPropertyStar_num = st.number_input("PreferredPropertyStar", min_value=3, max_value=5, value=3, step=1 )
NumberOfTrips_num = st.number_input("NumberOfTrips", min_value=1, max_value=22, value=1, step=1)
Passport_num = st.number_input("Passport", min_value=0, max_value=1, value=0, step=1)

PitchSatisfactionScore_num = st.number_input("PitchSatisfactionScore", min_value=1, max_value=5, value=1, step=1)
OwnCar_num = st.number_input("OwnCar", min_value=0, max_value=1, value=0,step=1)
NumberOfChildrenVisiting_num = st.number_input("NumberOfChildrenVisiting", min_value=0, max_value=3, value=0, step=1)
MonthlyIncome_num = st.number_input("MonthlyIncome in USD",min_value=1000, max_value=100000, value=1000, step=1)

# Assemble input into DataFrame
input_data = pd.DataFrame([{
    'TypeofContact': TypeofContact_category,
    'Occupation': Occupation_category,
    'Gender': Gender_category,
    'ProductPitched': ProductPitched_category,
    'MaritalStatus': MaritalStatus_category,
    'Designation': Designation_category,
    'Age': Age_num,
    'CityTier': CityTier_num,
    'DurationOfPitch': DurationOfPitch_num,
    'NumberOfPersonVisiting': NumberOfPersonVisiting_num,
    'NumberOfFollowups': NumberOfFollowups_num,
    'PreferredPropertyStar': PreferredPropertyStar_num,
    'NumberOfTrips': NumberOfTrips_num,
    'Passport': Passport_num,
    'PitchSatisfactionScore': PitchSatisfactionScore_num,
    'OwnCar': OwnCar_num,
    'NumberOfChildrenVisiting': NumberOfChildrenVisiting_num,
    'MonthlyIncome': MonthlyIncome_num
}])

# Predict button
if st.button("Predict Tourism pacakge customer "):
    prediction = model.predict(input_data)[0]
    st.subheader("Prediction Result:")
    st.success(f"Customer takes tourism package: **{prediction} **")
