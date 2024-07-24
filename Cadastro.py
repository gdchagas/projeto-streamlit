import streamlit as st
import pandas as pd
from datetime import date

#função para validação mínima dos dados
def gravar_dados(nome, data_nasc, tipo):
    if nome and dt_nascimento <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file: #"a" de append pra adc os clientes, "utf-8" pra acc acentos, Ç e etc
            file.write(f"{nome},{data_nasc},{tipo}\n") #configurar o arquivo csv no formato que escolhemos (separado por vírgula)
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📁"
)

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente:",
                     key="nome_cliente")

dt_nascimento = st.date_input("Digite a data de nascimento:", 
                              format="DD/MM/YYYY",
                              key="data_nascimento")

tipo_cliente = st.selectbox("Tipo do cliente:",
                            ["Pessoa jurídica", "Pessoa física"],
                            index=None,
                            placeholder="- - -")

btn_cadastrar = st.button("Cadastrar",
                          key="botao_cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nascimento, tipo_cliente])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="❌")