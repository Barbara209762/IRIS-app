import streamlit as st
import pandas as pd 

# Charger les données
data = pd.read_csv('Iris.csv') 

# Créer un titre
st.title("Mon premier tableau de bord Streamlit") 

# Afficher les données dans un tableau
st.table(data)


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données AUTO-MPG
@st.cache
def load_data():
    # Télécharger les données depuis seaborn
    df = sns.load_dataset("mpg").dropna()  # Supprimer les valeurs manquantes
    df["origin"] = df["origin"].map({1: "USA", 2: "Europe", 3: "Asia"})  # Mapper les origines
    return df

data = load_data()

# Titre et description
st.title("Tableau de bord interactif - Jeu de données AUTO-MPG")
st.markdown("""
Ce tableau de bord permet d'explorer le jeu de données AUTO-MPG. 
Utilisez les filtres pour explorer les relations entre différentes variables.
""")

# Afficher un aperçu des données
st.subheader("Aperçu des données")
st.dataframe(data.head())

# Filtrer les données par année du modèle
st.sidebar.header("Filtres")
year_range = st.sidebar.slider(
    "Année du modèle (model_year)", 
    int(data["model_year"].min()), 
    int(data["model_year"].max()), 
    (1970, 1980)
)
filtered_data = data[(data["model_year"] >= year_range[0]) & (data["model_year"] <= year_range[1])]

# Filtrer les données par origine
origins = st.sidebar.multiselect(
    "Origine du véhicule", 
    options=data["origin"].unique(), 
    default=data["origin"].unique()
)
filtered_data = filtered_data[filtered_data["origin"].isin(origins)]

# Afficher des statistiques
st.subheader("Statistiques descriptives")
st.write(filtered_data.describe())

# Visualisation : Distribution du MPG
st.subheader("Distribution de la consommation (MPG)")
fig, ax = plt.subplots()
sns.histplot(filtered_data["mpg"], bins=20, kde=True, ax=ax)
ax.set_title("Distribution de la consommation (MPG)")
st.pyplot(fig)

# Visualisation : Relation entre poids et consommation
st.subheader("Relation entre le poids et la consommation (MPG)")
fig, ax = plt.subplots()
sns.scatterplot(
    x="weight", y="mpg", hue="origin", style="cylinders", data=filtered_data, ax=ax
)
ax.set_title("Poids vs Consommation")
st.pyplot(fig)

# Graphique de tendance : Consommation moyenne par année
st.subheader("Évolution de la consommation moyenne par année")
mpg_by_year = filtered_data.groupby("model_year")["mpg"].mean()
st.line_chart(mpg_by_year)

# Télécharger les données filtrées
st.subheader("Téléchargez les données filtrées")
st.download_button(
    label="Télécharger les données en CSV",
    data=filtered_data.to_csv(index=False),
    file_name="auto_mpg_filtered.csv",
    mime="text/csv",
)






