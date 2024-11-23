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

import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']
data = pd.read_csv(url, delim_whitespace=True, names=column_names, na_values='?')

# Nettoyer les données
data = data.dropna()

# Titre de l'application
st.title("Analyse des données Auto MPG")

# Afficher les données
st.write("Voici un aperçu des données:")
st.write(data.head())

# Filtrer par année modèle
model_years = st.multiselect("Sélectionnez les années modèles", options=data["model year"].unique())
filtered_data = data[data["model year"].isin(model_years)]

# Sélectionner les colonnes pour les graphiques
x_axis = st.selectbox("Choisissez l'axe X", filtered_data.columns)
y_axis = st.selectbox("Choisissez l'axe Y", filtered_data.columns)

# Créer le graphique
fig, ax = plt.subplots()
ax.scatter(filtered_data[x_axis], filtered_data[y_axis])
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_title(f"Graphique de {y_axis} en fonction de {x_axis}")

# Afficher le graphique
st.pyplot(fig)











