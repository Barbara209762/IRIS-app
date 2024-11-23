import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données AUTO-MPG
@st.cache
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
st.bar_chart(cylinders_count)

# Créer un graphique MPG vs Poids
st.subheader("Relation entre MPG et Poids")
fig, ax = plt.subplots()
sns.scatterplot(x="weight", y="mpg", hue="origin", data=filtered_data, ax=ax)
ax.set_title("Consommation (MPG) vs Poids des voitures")
st.pyplot(fig)

# Ajouter un graphique linéaire interactif
st.subheader("Évolution de la consommation par année")
mpg_by_year = filtered_data.groupby("model_year")["mpg"].mean()
st.line_chart(mpg_by_year)

# Afficher des statistiques descriptives
st.subheader("Statistiques descriptives")
st.write(filtered_data.describe())

 







