import streamlit as st
import pandas as pd

# Sample nested data
nested_data = [
    pd.DataFrame({"Item": ["Apples", "Bananas"], "Qty": [5, 3]}),
    pd.DataFrame({"Item": ["Oranges", "Grapes"], "Qty": [2, 7]}),
    pd.DataFrame({"Item": ["Milk", "Bread"], "Qty": [1, 2]})
]

# Main DataFrame
main_df = pd.DataFrame({
    "Order ID": [101, 102, 103],
    "Customer": ["Alice", "Bob", "Charlie"],
    "Items": nested_data
})

# Convert nested DataFrame to clean, inline-expandable HTML
def df_to_expandable_html(nested_df):
    html_table = nested_df.to_html(index=False, border=0)
    html_table = html_table.replace('\n', '')  # Remove newlines
    return f"<details><summary style='cursor: pointer;'>View Items</summary>{html_table}</details>"

# Apply transformation
main_df["Items"] = main_df["Items"].apply(df_to_expandable_html)

# Display in Streamlit using safe HTML
st.markdown("### Orders Table with Expandable Item Details")
st.write(main_df.to_html(escape=False, index=False), unsafe_allow_html=True)
