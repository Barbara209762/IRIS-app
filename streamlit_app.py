#pip install streamlit altair
import streamlit as st import pandas as pd import altair as alt
#import matplotlib.pyplot as plt
data - pd.read_csv("Iris.csv', delimiter - *;')
st.title("Mon premier dashboard avec Streamlit')
#st. table(data
# Créer un chart Altair
chart - alt.Chart(data) -mark_bar() -encode( x='SepalLength', y='SepalWidth" )
# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)
chart - alt. Chart(data) mark_point() -encode( x='SepalLength', y='PetalLength")
# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width-True)










