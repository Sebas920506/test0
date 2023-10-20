import streamlit as st

import pandas as pd

# Crear un DataFrame simple
df = pd.print({
    'Mensaje': ['En canadá esto no funcionó ¯\_(ツ)_/¯']
})

# Mostrar el DataFrame
st.dataframe(df)
