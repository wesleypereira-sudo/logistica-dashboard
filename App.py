import streamlit as st
import pandas as pd

st.title("Painel de Logística - Versão 1")

st.subheader("1) Importar Disponibilidade")
disponibilidade = st.file_uploader("Selecione o arquivo de Disponibilidade", type=["xlsx"])

st.subheader("2) Importar Atribuição de Entregas")
atribuicao = st.file_uploader("Selecione o arquivo de Atribuição", type=["csv"])

st.subheader("3) Importar Call Up")
callup = st.file_uploader("Selecione o arquivo de Call Up", type=["csv"])

if st.button("Gerar Relatório"):
    st.success("Imports recebidos! A próxima versão vai cruzar os dados.")
