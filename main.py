import streamlit as st
import pickle

st.title('Titanic Survival')
st.sidebar.title('Input parameters')

pclass = st.sidebar.selectbox('Select Passenger Class', [1,2,3])
sex = st.sidebar.selectbox('Select Gender(0-Female, 1-Male)',[0,1])
age = st.sidebar.number_input('Age',0,100)
fare = st.sidebar.number_input('Fare',0.0,300.0)

with open('model.pkl','rb') as f:
    model = pickle.load(f)

if st.sidebar.button('Predict', key= 'predict_button'):
    input_data = [[pclass,sex,age,fare]]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success('The passenger survived')

    else:
        st.error('Low Survival chances')
    st.write(f'prediction:{prediction[0]}')

