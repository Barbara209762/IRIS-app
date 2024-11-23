import streamlit as st
import pandas as pd 

# Charger les données
data = pd.read_csv('Iris.csv',delimiter=';') 

# Créer un titre
st.title("Mon premier tableau de bord Streamlit") 

# Afficher les données dans un tableau

# st.write(data.head())

#pip install streamlit altair
import streamlit as st
import pandas as pd
import altair as alt
#import matplotlib.pyplot as plt


data =pd.read_csv('Iris.csv', delimiter = ';')
st.title('Mon premier dashboard avec Streamlit')
 #st. table(data)
import altair as alt
import pandas as pd

   # Créer un chart Altair
chart = alt.Chart(data).mark_bar().encode( x='SepalLength', y='SepalWidth')
# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)
                                           
chart = alt.Chart(data).mark_point().encode( x='SepalLength', y='PetalLength')
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
    ["Option iris", "Option data", "Option github"]
)

# Display selected option
st.write(f"You selected: {option}")



import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Charger les données Iris
@st.cache
def load_data():
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data["species"] = iris.target
    data["species"] = data["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
    return data

data = load_data()

# Titre du tableau de bord
st.title("Tableau de bord interactif : Jeu de données Iris")
st.markdown("""
Ce tableau de bord vous permet d'explorer le célèbre jeu de données Iris, 
utilisé pour la classification des espèces de fleurs en fonction de leurs dimensions.
""")
# Afficher un aperçu des données
st.subheader("Aperçu des données")
st.dataframe(data.head())

# Afficher des statistiques descriptives
st.subheader("Statistiques descriptives")
st.write(data.describe())

# Filtre par espèce
 st.sidebar.header("Filtres")
  = st.sidebar.multiselect(
    "Espèces sélectionnées", 
    options=data["species"].unique(), 
    default=data["species"].unique()
  )
 filtered_data = data[data["species"].isin(selected_species)]

 # Visualisation 1 : Nuage de points pour deux dimensions
 st.subheader("Relation entre deux dimensions des fleurs")
 x_axis = st.selectbox("Sélectionnez l'axe X :", data.columns[:-1])
 y_axis = st.selectbox("Sélectionnez l'axe Y :", data.columns[:-1])

 fig, ax = plt.subplots()
 sns.scatterplot(
    x=x_axis, 
    y=y_axis, 
    hue="species", 
 data=filtered_data, 
    ax=ax, 
    palette="viridis"
 )
 ax.set_title(f"{y_axis} vs {x_axis}")
 st.pyplot(fig)

 # Visualisation 2 : Distribution des dimensions
 st.subheader("Distribution des dimensions")
 dimension = st.selectbox("Sélectionnez une dimension :", data.columns[:-1])
 fig, ax = plt.subplots()
 sns.histplot(data=filtered_data, x=dimension, hue="species", kde=True, ax=ax, palette="viridis")
 ax.set_title(f"Distribution de {dimension}")
 st.pyplot(fig)

 # Télécharger les données filtrées
 st.subheader("Téléchargez les données filtrées")
 st.download_button(
 label="Télécharger les données en CSV",
 data=filtered_data.to_csv(index=False),
 file_name="iris_filtered.csv",
 mime="text/csv",
)







