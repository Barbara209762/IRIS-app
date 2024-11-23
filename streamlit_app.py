#pip install streamlit altair
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'species']
data = pd.read_csv(url, header=None, names=column_names)

# Titre de l'application
st.title("Exploration des données Iris")

# Afficher les données
st.write("Voici un aperçu des données:")
st.write(data.head())

# Sélectionner les colonnes pour les graphiques
x_axis = st.selectbox("Choisissez l'axe X", data.columns)
y_axis = st.selectbox("Choisissez l'axe Y", data.columns)

# Créer le graphique
fig, ax = plt.subplots()
sns.scatterplot(data=data, x=x_axis, y=y_axis, hue="species", ax=ax)
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_title(f"Graphique de {y_axis} en fonction de {x_axis}")

# Afficher le graphique
st.pyplot(fig)

