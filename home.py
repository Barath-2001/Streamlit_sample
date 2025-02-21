import streamlit as st

continents_countries = {
    'Africa': ['Egypt', 'Kenya', 'Nigeria'],
    'Asia': ['China', 'India', 'Japan'],
    'Europe': ['France', 'Germany', 'Italy'],
}

st.title('Continent and Country Selection')

selected_continent = st.selectbox('Select Continent', 
                                  options=['Select a continent'] + list(continents_countries.keys()),
                                  key='continent_key')

if selected_continent == 'Select a continent':
    countries = ['Select a country']
else:
    countries = continents_countries.get(selected_continent, [])

selected_country = st.selectbox('Select Country', 
                                options=['Select a country'] + countries,
                                key='country_key')

if selected_continent != 'Select a continent' and selected_country != 'Select a country':
    st.write(f"You selected {selected_country} in {selected_continent}.")
elif selected_continent != 'Select a continent':
    st.write(f"You selected {selected_continent}. Please select a country.")
else:
    st.write("Please select a continent and a country.")
