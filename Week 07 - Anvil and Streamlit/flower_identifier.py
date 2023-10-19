import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
@st.cache
def load_data():
    dataset = pd.read_csv(url, names=names)
    return dataset
dataset = load_data()

st.title("IRIS flower machine learning model")
if st.checkbox('Show dataframe'):
    dataset
    
fig = px.scatter(dataset, x="sepal-width", y="sepal-length", color="class",
                 size='petal-length', hover_data=['petal-width'],width=800, height=400)
st.plotly_chart(fig)