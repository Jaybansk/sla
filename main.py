import os
import pandas as pd
import streamlit as st


# st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )   
# Define the pages
data = st.Page("streamlit/pages/data.py", title="Data")
summary = st.Page("streamlit/pages/summary.py", title="Summary")
# page_3 = st.Page("page_3.py", title="Page 3", icon="🎉")

# Set up navigation
pg = st.navigation([data, summary])


# Run the selected page
pg.run()