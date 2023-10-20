import streamlit as st

import pandas as pd

# Crear un DataFrame simple
df = pd.DataFrame({
    'Mensaje': ['En canadá esto no funcionó ¯\_(ツ)_/¯']
})

# Mostrar el DataFrame
st.dataframe(df)
