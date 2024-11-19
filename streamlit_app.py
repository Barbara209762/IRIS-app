import streamlit as st
import pandas as pd 

# Charger les données
data = pd.read_csv('Iris.csv',delimiter=';') 

# Créer un titre
st.title("Mon premier tableau de bord Streamlit") 

# Afficher les données dans un tableau
st.table(data)
st.write(data.head())
