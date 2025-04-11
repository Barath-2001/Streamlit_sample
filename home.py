import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Sample DataFrame with expandable content
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Comments": [
        "This is a long comment that should be expandable in the table.",
        "Another long comment that provides detailed feedback on performance.",
        "Short one."
    ]
}

df = pd.DataFrame(data)

st.title("Expandable Column in Streamlit Data Table")

# Create grid options
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_column("Comments", autoHeight=True, wrapText=True)
grid_options = gb.build()

# Render interactive grid
AgGrid(
    df,
    gridOptions=grid_options,
    enable_enterprise_modules=False,
    allow_unsafe_jscode=True,
    theme="streamlit"
)
