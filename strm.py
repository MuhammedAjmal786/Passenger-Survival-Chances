import pandas as pd
import numpy as np
import streamlit as st
import pickle

st.title('Survival Prediction')

Age=st.number_input('Age')
Gender=st.selectbox('Gender',['Male','Female'])
Class=st.radio('Class',['Economy', 'First', 'Business'])
Seat_Type=st.radio('Seat Type',['Window', 'Middle', 'Aisle'])
Fare_Paid=st.number_input('Fare Paid')

input_Data={
    'Age':Age,
    'Gender':Gender,
    'Class':Class,
    'Seat_Type':Seat_Type,
    'Fare_Paid':Fare_Paid
    }
inputData=pd.DataFrame([input_Data])

Genco={'Female':0, 'Male':1}
Cenco={'Economy':0, 'First':1, 'Business':2}
Senco={'Window':2, 'Middle':1, 'Aisle':0}

inputData['Gender']=inputData['Gender'].map(Genco)
inputData['Class']=inputData['Class'].map(Cenco)
inputData['Seat_Type']=inputData['Seat_Type'].map(Senco)

model=pickle.load(open('model.pkl','rb'))

prediction=model.predict(inputData)

if st.button('Submit'):
    if prediction[0]==1:
        st.success('Thank God, Survived')
    else:
        st.error('Sory, We lost them')
    