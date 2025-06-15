import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
import random
from streamlit_autorefresh import st_autorefresh

# --- CONFIGURAÇÃO STREAMLIT ---
st.set_page_config(page_title="Simulador Solar", layout="wide")
st_autorefresh(interval=5000, key="refresh")  # Atualiza a cada 5 segundos

# --- BANCO DE DADOS ---
conn = sqlite3.connect("solar_data.db", check_same_thread=False)
c = conn.cursor()

# Cria tabela (se não existir)
c.execute('''CREATE TABLE IF NOT EXISTS simulacoes (
    timestamp TEXT,
    id_casa INTEGER,
    consumo_kwh REAL,
    geracao_kwh REAL,
    excedente REAL
)''')
conn.commit()

# --- SIMULAÇÃO ---
st.title("🔆 Simulador de Energia Solar em Tempo Real")

potencia_kwp = st.slider("Potência do sistema (kWp)", 1.0, 10.0, 3.5, 0.5)
eficiencia = 0.8
horas_sol = random.uniform(3.5, 6.0)  # Simula variação de sol

# Simular 10 casas com consumo aleatório (substituir por seus dados reais)
for id_casa in range(1, 11):
    consumo = random.uniform(8, 20)  # Consumo simulado (kWh)
    geracao = potencia_kwp * horas_sol * eficiencia
    excedente = geracao - consumo
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    c.execute("INSERT INTO simulacoes VALUES (?, ?, ?, ?, ?)", 
              (timestamp, id_casa, consumo, geracao, excedente))
conn.commit()

# --- VISUALIZAÇÃO ---
df = pd.read_sql_query("SELECT * FROM simulacoes", conn)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df_latest = df.sort_values("timestamp").groupby("id_casa").tail(1)

st.subheader("📊 Última Geração por Casa")
st.dataframe(df_latest)

# Gráfico comparando consumo x geração
st.line_chart(df_latest.set_index("id_casa")[["consumo_kwh", "geracao_kwh"]])
