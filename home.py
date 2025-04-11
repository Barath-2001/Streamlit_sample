import streamlit as st
import pandas as pd


# Nested data in one of the columns
nested_data = [
    pd.DataFrame({"Item": ["Apples", "Bananas"], "Qty": [5, 3]}),
    pd.DataFrame({"Item": ["Oranges", "Grapes"], "Qty": [2, 7]}),
    pd.DataFrame({"Item": ["Milk", "Bread"], "Qty": [1, 2]})
]

main_df = pd.DataFrame({
    "Order ID": [101, 102, 103],
    "Customer": ["Alice", "Bob", "Charlie"],
    "Items": nested_data
})

def df_to_expandable_html(nested_df):
    # Convert nested df to HTML
    html_table = nested_df.to_html(index=False)
    # Wrap it in <details> tag for expandability
    return f"<details><summary>View Items</summary>{html_table}</details>"

main_df["Items"] = main_df["Items"].apply(df_to_expandable_html)

st.title("🧾 Orders with Expandable Items")

# Render with HTML for expandable effect
st.write(main_df.to_html(escape=False), unsafe_allow_html=True)
