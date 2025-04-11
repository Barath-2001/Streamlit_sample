import streamlit as st
import pandas as pd

# Sample data with a long text column
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Details": [
        "This is a long description about Alice. She is working on multiple projects in data science, machine learning, and AI.",
        "Bob has a very detailed history in backend development, especially with Python and FastAPI.",
        "Charlie is involved in frontend development with React and has a strong grasp on UI/UX principles."
    ]
}

df = pd.DataFrame(data)

# Convert the 'Details' column into expandable HTML blocks
df["Details"] = df["Details"].apply(lambda x: f"<details><summary>Click to expand</summary><p>{x}</p></details>")

st.title("📊 Expandable Column in DataFrame Table")

# Display the styled table
st.write(df.to_html(escape=False), unsafe_allow_html=True)
