import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# Coloque logo aqui, antes de qualquer outro comando streamlit
#st.set_page_config(page_title="🤖 EnergiA - Agente Inteligente", layout="wide")

# Configura sua API key (coloque sua real, e cuidado para não expor)
os.environ["OPENAI_API_KEY"] = "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"

# Inicializa banco e LLM
db = SQLDatabase.from_uri("sqlite:///smartcity_laguna.db")
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=False)  # verbose=False pra ficar clean

# Função para executar a pergunta e retornar resposta (sem printar direto)
def perguntar_agente(pergunta):
    try:
        resposta = db_chain.run(pergunta)
        return resposta
    except Exception as e:
        return f"Erro: {str(e)}"

def app_agente():
    #st.set_page_config(page_title="🤖 EnergiA - Agente Inteligente", layout="wide")

    st.title("🤖 EnergiA - Seu Assistente de Energia")
    st.markdown(
        """
        **Pergunte sobre consumo, geração, sensores e alertas no sistema de energia da Smart City Laguna.**
        
        Exemplos:
        - Qual casa mais gerou energia?
        - Qual casa teve maior consumo?
        - Quais casas estão com excedente positivo?
        """
    )

    # Caixa de entrada de texto para perguntas customizadas
    pergunta = st.text_input("💬 Faça uma pergunta personalizada:")

    # Área para exibir a resposta do texto input ou botões
    resposta_area = st.empty()

    # Se enviou pergunta via input, processa e mostra
    if pergunta:
        with st.spinner("Consultando base de dados..."):
            resposta = perguntar_agente(pergunta)
            if resposta.startswith("Erro:"):
                st.error(resposta)
            else:
                resposta_area.markdown(f"**🤖 Resposta:** {resposta}")

    st.markdown("---")
    st.write("Ou selecione uma ação rápida:")

    # Botões em colunas para melhor layout
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🛰️ Monitorar sensores"):
            with st.spinner("Consultando sensores..."):
                resposta = perguntar_agente("Mostre os dados dos sensores.")
                if resposta.startswith("Erro:"):
                    st.error(resposta)
                else:
                    resposta_area.markdown(f"**🤖 Resposta:** {resposta}")

        if st.button("💡 Dicas de economia"):
            with st.spinner("Buscando dicas..."):
                resposta = perguntar_agente("Me dê dicas para economizar energia.")
                if resposta.startswith("Erro:"):
                    st.error(resposta)
                else:
                    resposta_area.markdown(f"**🤖 Resposta:** {resposta}")

    with col2:
        if st.button("📊 Consumo hoje"):
            with st.spinner("Consultando consumo do dia..."):
                resposta = perguntar_agente("Qual foi o consumo de energia hoje?")
                if resposta.startswith("Erro:"):
                    st.error(resposta)
                else:
                    resposta_area.markdown(f"**🤖 Resposta:** {resposta}")

        if st.button("📈 Previsão de consumo"):
            with st.spinner("Gerando previsão..."):
                resposta = perguntar_agente("Faça uma previsão do consumo futuro.")
                if resposta.startswith("Erro:"):
                    st.error(resposta)
                else:
                    resposta_area.markdown(f"**🤖 Resposta:** {resposta}")

    with col3:
        if st.button("💰 Insights de gastos"):
            with st.spinner("Analisando gastos..."):
                resposta = perguntar_agente("Quais os insights sobre os gastos de energia?")
                if resposta.startswith("Erro:"):
                    st.error(resposta)
                else:
                    resposta_area.markdown(f"**🤖 Resposta:** {resposta}")

        if st.button("📄 Gerar relatório"):
            with st.spinner("Gerando relatório..."):
                resposta = perguntar_agente("Gere um relatório de consumo e geração.")
                if resposta.startswith("Erro:"):
                    st.error(resposta)
                else:
                    resposta_area.markdown(f"**🤖 Resposta:** {resposta}")


