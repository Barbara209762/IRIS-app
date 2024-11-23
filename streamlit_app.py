import streamlit as st
import pandas as pd

# Charger les données Iris
@st.cache
def load_data():
    return sns.load_dataset("iris")

data = load_data()

# Titre et introduction
st.title("Tableau de bord interactif - Jeu de données Iris")
st.markdown("""
Ce tableau de bord vous permet d'explorer le jeu de données Iris. Utilisez les *filtres* pour sélectionner les espèces et visualiser les relations entre les différentes caractéristiques.
""")

# Sidebar pour les filtres
st.sidebar.header("Filtres")
selected_species = st.sidebar.multiselect(
    "Sélectionnez les espèces :",
    options=data["species"].unique(),
    default=data["species"].unique(),
)

# Filtrer les données
filtered_data = data[data["species"].isin(selected_species)]

# Afficher les données
st.subheader("Aperçu des données")
st.write(f"Nombre d'observations : {len(filtered_data)}")
st.dataframe(filtered_data)

# Afficher des statistiques descriptives
st.subheader("Statistiques descriptives")
st.write(filtered_data.describe())

# Visualisation 1 : Distribution de la longueur du sépale
st.subheader("Distribution de la longueur du sépale")
fig, ax = plt.subplots()
sns.histplot(filtered_data["sepal_length"], bins=10, kde=True, ax=ax, color="blue")
ax.set_title("Distribution de la longueur du sépale")
st.pyplot(fig)

# Visualisation 2 : Longueur et largeur du pétale
st.subheader("Relation entre la longueur et la largeur du pétale")
fig, ax = plt.subplots()
sns.scatterplot(
    x="petal_length",
    y="petal_width",
    hue="species",
    style="species",
    data=filtered_data,
    ax=ax,
)
ax.set_title("Longueur vs Largeur du pétale")
st.pyplot(fig)

# Visualisation 3 : Boxplot des longueurs de sépales par espèce
st.subheader("Boxplot : Longueur des sépales par espèce")
fig, ax = plt.subplots()
sns.boxplot(x="species", y="sepal_length", data=filtered_data, ax=ax)
ax.set_title("Longueur des sépales par espèce")
st.pyplot(fig)

# Visualisation 4 : Moyenne des longueurs de pétales par espèce
st.subheader("Moyenne des longueurs de pétales par espèce")
avg_petal_length = filtered_data.groupby("species")["petal_length"].mean()
st.bar_chart(avg_petal_length)

# Téléchargement des données filtrées
st.subheader("Téléchargez les données filtrées")
st.download_button(
    label="Télécharger les données en CSV",
    data=filtered_data.to_csv(index=False),
    file_name="iris_filtered.csv",
    mime="text/csv",
)

 







