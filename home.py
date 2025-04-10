import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Sample DataFrame
df = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Details": [
        "Alice is working on a long project about natural language processing.",
        "Bob's report includes multiple modules and dependencies for data processing.",
        "Charlie is handling the deployment phase, monitoring logs and performance."
    ]
})

# Build grid options
gb = GridOptionsBuilder.from_dataframe(df)

# Make 'Details' column expandable
gb.configure_column(
    "Details",
    cellRenderer="""
    function(params) {
        const text = params.value;
        const short = text.length > 50 ? text.substring(0, 50) + "..." : text;
        return `<details><summary>${short}</summary><div style="white-space: normal;">${text}</div></details>`;
    }
    """,
    autoHeight=True,
    wrapText=True
)

# Build and display the grid
gridOptions = gb.build()

AgGrid(
    df,
    gridOptions=gridOptions,
    allow_unsafe_jscode=True,  # Required for the HTML inside cell
    fit_columns_on_grid_load=True
)
