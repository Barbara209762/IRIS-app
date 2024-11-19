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


import matplotlib.pyplot as plt

# Create a scatter plot
fig, ax = plt.subplots()
for s in species:
    species_data = filtered_data[filtered_data['species'] == s]
    ax.scatter(
        species_data[x_iris], 
        species_data[y_data], 
        label=s
    )

ax.set_xlabel(x_iris)
ax.set_ylabel(y_data)
ax.legend()
ax.set_title("Iris Dataset Scatter Plot")

# Show the plot in Streamlit
st.pyplot(fig)





