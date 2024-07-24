import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv")

st.set_page_config(
    page_title="Consulta de clientes",
    page_icon="📁"
)

st.title("Clientes cadastrados")
st.divider()

st.dataframe(dados)