import streamlit as st
import pandas as pd

# Sample data for continents and countries
continents_countries = {
    'Africa': ['Egypt', 'Kenya', 'Nigeria', 'South Africa'],
    'Asia': ['China', 'India', 'Japan', 'Thailand'],
    'Europe': ['France', 'Germany', 'Italy', 'United Kingdom'],
    'North America': ['Canada', 'Mexico', 'United States'],
    'South America': ['Argentina', 'Brazil', 'Chile', 'Peru'],
    'Oceania': ['Australia', 'New Zealand', 'Fiji', 'Papua New Guinea']
}

@st.cache_data
def load_data():
    return pd.DataFrame([(continent, country) 
                         for continent, countries in continents_countries.items() 
                         for country in countries], 
                        columns=['Continent', 'Country'])

df = load_data()

@st.fragment
def continent_dropdown():
    return st.selectbox('Select Continent', 
                        options=[''] + list(continents_countries.keys()),
                        key='continent_key')

@st.fragment
def country_dropdown(continent):
    countries = continents_countries.get(continent, [])
    return st.selectbox('Select Country', 
                        options=[''] + countries,
                        key='country_key',
                        disabled=not countries)

st.title('Continent and Country Selection')

col1, col2 = st.columns(2)

with col1:
    selected_continent = continent_dropdown()

with col2:
    selected_country = country_dropdown(selected_continent)

if selected_continent and selected_country:
    st.write(f"You selected {selected_country} in {selected_continent}.")
elif selected_continent:
    st.write(f"You selected {selected_continent}. Please select a country.")
else:
    st.write("Please select a continent and a country.")
