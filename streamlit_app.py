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



# Charger les données AUTO-MPG
@st.cache
def load_data():
    df = sns.load_dataset("mpg").dropna()
    # Charger depuis seaborn et supprimer les valeurs manquantes
    df["origin"] = df["origin"].map({1: "USA", 2: "Europe", 3: "Asia"})  
    # Remplacer les codes par des labels
    return df

data = load_data()

# Titre du tableau de bord
st.title("Tableau de bord interactif - Jeu de données AUTO-MPG")
st.markdown("""
Ce tableau de bord permet d'explorer le jeu de données AUTO-MPG. 
Utilisez les graphiques pour analyser les relations entre les caractéristiques des voitures.
""")

# Afficher un aperçu des données
st.subheader("Aperçu des données")
st.dataframe(data)

# Filtres interactifs
st.sidebar.header("Filtres")
years = st.sidebar.slider(
    "Années des modèles (model_year)",
    int(data["model_year"].min()),
    int(data["model_year"].max()),
    (1970, 1980)
)
origins = st.sidebar.multiselect(
    "Origine des véhicules",
    options=data["origin"].unique(),
    default=data["origin"].unique()
)

# Appliquer les filtres
filtered_data = data[(data["model_year"] >= years[0]) & (data["model_year"] <= years[1])]
filtered_data = filtered_data[filtered_data["origin"].isin(origins)]

# Graphique 1 : Histogramme de la consommation (MPG)
st.subheader("Distribution de la consommation (MPG)")
fig, ax = plt.subplots()
sns.histplot(filtered_data["mpg"], bins=20, kde=True, color="blue", ax=ax)
ax.set_title("Histogramme de la consommation (MPG)")
st.pyplot(fig)

# Graphique 2 : Relation entre poids et consommation (MPG)
st.subheader("Relation entre le poids et la consommation (MPG)")
fig, ax = plt.subplots()
sns.scatterplot(
    x="weight", 
    y="mpg", 
    hue="origin", 
    style="cylinders", 
    data=filtered_data, 
    ax=ax
)
ax.set_title("Consommation (MPG) vs Poids")
st.pyplot(fig)

# Graphique 3 : Évolution de la consommation moyenne par année
st.subheader("Évolution de la consommation moyenne par année")
avg_mpg_by_year = filtered_data.groupby("model_year")["mpg"].mean()
st.line_chart(avg_mpg_by_year)

# Graphique 4 : Boxplot des cylindrées par origine
st.subheader("Comparaison des cylindrées par origine")
fig, ax = plt.subplots()
sns.boxplot(x="origin", y="displacement", data=filtered_data, ax=ax)
ax.set_title("Cylindrées par origine")
st.pyplot(fig)

# Télécharger les données filtrées
st.subheader("Téléchargez les données filtrées")
st.download_button(
    label="Télécharger les données en CSV",
    data=filtered_data.to_csv(index=False),
    file_name="auto_mpg_filtered.csv",
    mime="text/csv",
)






