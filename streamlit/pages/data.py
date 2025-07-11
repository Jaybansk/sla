import os
import streamlit as st
import pandas as pd

st.write("Data")

file_path = './streamlit/data/issues.csv'

file_name = os.path.basename(file_path)
df = pd.read_csv(file_path)

st.markdown(f'''
            # Customer Reported Issues
            Data from the file **{file_name}**.
''')

st.write(df)
