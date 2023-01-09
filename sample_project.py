import pandas as pd
import matplotlib.pyplot as plt
import math_tools as mt
import streamlit as st 
import seaborn as sns

st.header('Titanic Survaivability Analysis')
st.subheader('this is smaller')
st.write('A **short** explanation of the project.')

titanic_df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')

st.write('the imports: ')
st.code('''
import pandas as pd
import matplotlib.pyplot as plt
import math_tools as mt
import streamlit as st 
import seaborn as sns
''')

if st.sidebar.checkbox('Show raw data'):
    st.write('The row data:')
    st.write(titanic_df)

st.subheader('Correlation matrix')

col_3, col_4, col_5 = st.columns(3)

with col_4:
    titanic_corr = titanic_df.corr()
    fig, ax = plt.subplots(figsize=(10,6))
    sns.heatmap(titanic_corr, annot = True, ax=ax)
    st.write(fig)

st.subheader('Plots')

col_1, col_2 = st.columns(2)

with col_1:
    fig, ax = plt.subplots(figsize=(10,6))
    titanic_df.Age.hist()
    st.write(fig)
    st.caption('Age distribution')

with col_2:
    fig, ax = plt.subplots(figsize=(10,6))
    titanic_df.Fare.hist()
    st.write(fig)
    st.caption('Fare distribution')