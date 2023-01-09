import pandas as pd
import matplotlib.pyplot as plt
import math_tools as mt
import streamlit as st 
import seaborn as sns

st.header('Titanic Survaivability Analysis')
st.subheader('this is smaller')
st.write('A **short** explanation of the project.')

titanic_df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')

st.write('The row data:')
st.write(titanic_df)

st.subheader('Correlation matrix')
titanic_corr = titanic_df.corr()
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(titanic_corr, annot = True, ax=ax)
st.write(fig)

st.subheader('Plots')
fig, ax = plt.subplots(figsize=(10,6))
titanic_df.Age.hist()
st.write(fig)