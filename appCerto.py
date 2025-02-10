import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Analisador de Dados - Excel", layout="wide")

# Título da aplicação
st.title("📊 Ensaios de Teste de 5 Ciclos")

# Upload do arquivo
arquivo = st.file_uploader("Selecione um arquivo Excel", type=["xlsx", "xls"])

if arquivo:
    try:
        # Obtendo os nomes das planilhas
        xls = pd.ExcelFile(arquivo, engine='openpyxl')
        planilhas = xls.sheet_names

        # Se houver mais de uma aba, permitir seleção
        aba_selecionada = st.selectbox("Selecione a aba:", planilhas)

        # Carregando dados da aba selecionada
        df = pd.read_excel(xls, sheet_name=aba_selecionada, skiprows=7)

        # Exibir as colunas encontradas
        st.write("📌 **Colunas disponíveis:**", df.columns.tolist())

        # Permitir ao usuário selecionar as colunas desejadas
        col_x = st.selectbox("Selecione a coluna para o eixo X:", df.columns)
        col_y = st.selectbox("Selecione a coluna para o eixo Y:", df.columns)

        # Exibir as primeiras linhas do DataFrame
        st.subheader("📋 Dados Carregados")
        st.dataframe(df.head())

        # Criar gráfico interativo
        st.subheader("📈 Gráfico de Dados")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df[col_x], df[col_y], marker='o', linestyle='-', color='b', label=f'{col_x} x {col_y}')

        # Configuração do gráfico
        ax.set_xlabel(col_x)
        ax.set_ylabel(col_y)
        ax.set_title(f'Gráfico de {col_x} x {col_y}')
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.7)

        # Exibir gráfico no Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Erro ao processar o arquivo: {e}")
