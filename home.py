import streamlit as st
import pandas as pd
from streamlit_slickgrid import slickgrid

# Sample data
df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Project A", "Project B", "Project C"],
    "description": ["This is a very long description that would normally overflow...", 
                   "Another lengthy description with details...",
                   "Yet another detailed explanation that needs more space..."]
})

# Configure SlickGrid options
grid_options = {
    "enableCellNavigation": True,
    "enableColumnResize": True,
    "autoHeight": False,
    "rowHeight": 45,  # Taller rows to accommodate expandable content
    "explicitInitialization": True
}

# Column definitions with custom formatter for expandable content
column_definitions = [
    {"id": "id", "name": "ID", "field": "id", "sortable": True},
    {"id": "name", "name": "Name", "field": "name", "sortable": True},
    {
        "id": "description", 
        "name": "Description", 
        "field": "description", 
        "sortable": True,
        "formatter": "ExpandableFormatter",  # Custom formatter
        "formatterOptions": {
            "maxLength": 30  # Show only first 30 chars initially
        }
    }
]

# Display the grid
result = slickgrid(
    df,
    grid_options=grid_options,
    column_definitions=column_definitions,
    key="my_grid"
)

# Show selected data
if result:
    st.write("Selected:", result)
