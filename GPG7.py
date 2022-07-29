import streamlit as st
import pandas as pd
from tabulate import tabulate
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Gender Pay Gap
This app predicts the Pay!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
  year = st.sidebar.slider('Year', 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017)
  gender = st.sidebar.slider('Gender', female, male)
  data = {'year': year,'gender': gender}
  features = pd.DataFrame(data, index=[0])
  return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

Pay = pd.read_csv('https://raw.githubusercontent.com/cheryllim1/Gender-Pay-Gap-2004---2017/main/earning.csv')
X = Pay.drop('pay',axis = 1)
Y = Gender['gender']

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Year and Gender')
st.write(pay)
