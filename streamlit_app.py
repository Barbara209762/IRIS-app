#pip install streamlit altair
import streamlit as st 
import pandas as pd
import altair as alt

data=pd.read_csv("Iris.csv", delimiter = ';')
st.title("Mon premier dashboard avec Streamlit")
#st. table(data)
chart = alt.Chart(data).mark_bar().encode(
    alt.X('SepalLength:Q', bin=True),  # Specify 'SepalLength' as quantitative and bin it
    alt.Y('count()') # Count the number of occurrences in each bin
    # y='SepalWidth'  <- Remove this or it might cause an error. Bar chart with x='SepalLength', y='SepalWidth' is unusual
) 

chart
# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_point().encode(
    x='SepalLength',  
    y='PetalLength' 
)

chart
# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)


import streamlit as st

# Title for the main app
st.title("Main App Area")

# Title for the sidebar
st.sidebar.title("Sidebar")

# Add widgets to the sidebar
option = st.sidebar.selectbox(
    "Select an option:",
    ["Option 1:iris", "Option 2;data", "Option 3;analytics"]
)

# Display selected option
st.write(f"You selected: {option}")
      
       


import pandas as pd


# Charger les données Iris
@st.cache
def load_iris_data():
 return sns.load_dataset("iris")
   


# Titre et introduction
st.title("Tableau de bord interactif - Jeu de données Iris")
st.markdown("""
Ce tableau de bord vous permet d'explorer le jeu de données Iris. Utilisez les *filtres* pour sélectionner les espèces et visualiser les relations entre les différentes caractéristiques.
""")

# Sidebar pour les filtres
st.sidebar.header("Filtres")
selected_species = st.sidebar.multiselect(


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







