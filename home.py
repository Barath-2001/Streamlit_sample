import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "ID": [1, 2, 3],
    "Details": [
        "This is a long description that should be shown in a dropdown when clicked.",
        "Another verbose field containing JSON or structured data you might want to expand.",
        "Something else quite long and informative."
    ]
})

for index, row in df.iterrows():
    with st.expander(f"Row {row['ID']}"):
        st.write(row["Details"])
