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



import numpy as np


st.title("Simulation[tm]")
st.write("Here is our super important simulation")

st.sidebar.markdown("## Controls")
st.sidebar.markdown("You can *change* the values to change the chart.")
x = st.sidebar.slider('Slope', min_value=0.01, max_value=0.10, step=0.01)
y = st.sidebar.slider('Noise', min_value=0.01, max_value=0.10, step=0.01)

st.write(f"x={x} y={y}")
values = np.cumprod(1 + np.random.normal(x, y, (100, 10)), axis=0)

values = np.array([[1, 2, 3], [4, 5, 6]])  # A 2x3 array

for i in range(values.shape[1]):  # Loop over columns (0, 1, 2)
    column = values[:, i]  # Get the i-th column
    print(f"Column {i}: {column}"):
    

st.pyplot()


 







