import streamlit as st
import pandas as pd
from src.utils import load_model

st.title(" Mall Customer Segmentation App")

# model = load_model("models/kmeans_model.pkl")

st.write("Upload customer data or use sample dataset")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    labels = model.predict(X)

    df['Cluster'] = labels

    st.write("### Clustered Data")
    st.write(df)

    st.bar_chart(df['Cluster'].value_counts())
