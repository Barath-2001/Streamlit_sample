import streamlit as st
import pandas as pd

# Sample data
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Comments": [
        "This is a long comment that should be expandable in the table.",
        "Another long comment with detailed performance notes.",
        "Short one."
    ]
}

df = pd.DataFrame(data)

st.title("Expandable Comments (No Extra Libraries)")

for index, row in df.iterrows():
    with st.expander(f"Row {row['ID']}: {row['Name']}"):
        st.write(row["Comments"])
