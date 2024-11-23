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
st.title("Main App visualisation")

# Title for the sidebar
st.sidebar.title("Sidebar")

# Add widgets to the sidebar
option = st.sidebar.selectbox(
    "Select an option:",
    ["Option 1:iris", "Option 2;data", "Option 3;analytics"]
)

import streamlit as st
import pandas as pd

# Charger les données
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'species']
data = pd.read_csv(url, header=None, names=column_names)

# Vérifier les colonnes
if 'species' not in data.columns:
    st.error("La colonne 'species' n'existe pas dans les données.")
else:
    # Titre de l'application
    st.title("Exploration des données Iris")

    # Afficher les données
    st.write("Voici un aperçu des données:")
    st.write(data.head())

    # Sélectionner les colonnes pour les graphiques
    x_axis = st.selectbox("Choisissez l'axe X", data.columns)
    y_axis = st.selectbox("Choisissez l'axe Y", data.columns)

    # Créer le graphique
    st.write(f"Graphique de {y_axis} en fonction de {x_axis}")
    st.line_chart(data[[x_axis, y_axis]])

    # Filtrer par espèce
    species = st.multiselect("Sélectionnez les espèces", options=data["species"].unique())
    filtered_data = data[data["species"].isin(species)]
    st.write("Données filtrées:")
    st.write(filtered_data)







