import streamlit as st
import pandas as pd 

# Charger les données
data = pd.read_csv('Iris.csv',delimiter=';') 

# Créer un titre
st.title("Mon premier tableau de bord Streamlit") 

# Afficher les données dans un tableau

st.write(data.head())

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
 chart = alt.Chart(data).mark_bar().encode( x='SepalLength', y='SepalWidth" )
# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)
                                           
chart = alt.Chart(data).mark_point().encode( x='SepalLength', y='PetalLength')
# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)




