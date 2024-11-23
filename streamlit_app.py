import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données AUTO-MPG
@st.cache_data  # Use st.cache_data instead of st.cache
def load_data():
    # Charger les données depuis seaborn
    return sns.load_dataset('mpg').dropna()

data = load_data()

# Titre du tableau de bord
st.title("Dashboard interactif : Analyse du jeu de données AUTO-MPG")

# Afficher les données dans un tableau interactif
st.subheader("Aperçu des données")
st.write(data.head())

# Ajouter un filtre pour l'année du modèle
year_filter = st.slider("Filtrer par année du modèle :", int(data["model_year"].min()), int(data["model_year"].max()), (1970, 1980))
filtered_data = data[(data["model_year"] >= year_filter[0]) & (data["model_year"] <= year_filter[1])]

st.write(f"Nombre de voitures sélectionnées : {len(filtered_data)}")

# Créer un graphique des cylindres
st.subheader("Distribution des cylindres")
cylinders_count = filtered_data["cylinders"].value_counts()
st.bar_chart(cylinders_count) # Corrected this line

 







