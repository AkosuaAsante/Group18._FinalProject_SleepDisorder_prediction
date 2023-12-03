import streamlit as st
import pickle 
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler,OneHotEncoder



model=pickle.load(open('xgmomodel.pkl','rb'))

def preprocess_input(BMIGroup,PhysicalActivityLevel,Age,StressLevel,HeartRate,
                     SleepDuration,Gender,BloodPressure):
    BMI_Group=['Overweight', 'Normal']
    Gender_values=['Male' ,'Female']
    le_BMI= LabelEncoder()
    le_Gender=LabelEncoder()

    le_BMI.fit(BMI_Group)
    le_Gender.fit(Gender_values)

    BMI_encoder=le_BMI.transform([BMIGroup])[0]
    Gender_encoder=le_Gender.transform([Gender])[0]

    input_features = np.array([[BMI_encoder, PhysicalActivityLevel,Age, 
                            StressLevel,HeartRate,SleepDuration,Gender_encoder,BloodPressure]])
    sc=StandardScaler()
    input_features_scaled = sc.fit_transform(input_features)
    return input_features_scaled


def show_predict():
    st.title('Predict Sleep Disorder')
    BMI_Group=['Overweight' ,'Normal']
    Genders=['Male','Female']
    Bloodpressure=[0,1]

    BMIGroup=st.selectbox("BMI Group",BMI_Group)
    PhysicalActivity = st.number_input("Physical Activity Level:", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
    Age=st.slider("Age",10,100,10)
    StressLevel=st.slider("Stress Level",1,10,1)
    HeartRate=st.slider("Heart Rate",50,100,50)
    SleepDuration=st.slider("Sleep Duration:",1,24,1)
    Gender=st.selectbox("Gender",Genders)
    BloodPressure=st.selectbox("BloodPressure",Bloodpressure)
    
    input_features = preprocess_input(BMIGroup,PhysicalActivity,Age,StressLevel,
                                      HeartRate,SleepDuration,Gender,BloodPressure)
    Sleep_Disorder=[["None","Sleep Apnea","Insomia"]]
    prediction= model.predict(input_features)

    if prediction==0:
        predicted="Insomia"
    elif prediction==1:
        predicted="None"
    elif prediction==2:
        predicted="Sleep Apnea"

    st.write("Predicted Sleep Disorder Class:",predicted)
    st.write("Warning:Should Not Be Used Without Medical Consult")

show_predict()
