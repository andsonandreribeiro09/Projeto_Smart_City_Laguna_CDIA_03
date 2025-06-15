# ⚡ Gêmeo Digital - Smart City Laguna  CDIA 03


Este projeto desenvolve um **Gêmeo Digital para residências inteligentes**, com foco na **análise, previsão e otimização do consumo de energia elétrica**. 
Utiliza dados simulados de sensores por cômodo, aplica técnicas de **Machine Learning** e oferece visualizações interativas via **Streamlit**.

---

[![Assista no YouTube](https://img.shields.io/badge/🎥%20Ver%20no%20YouTube-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=P8ynA2q_MaY)

---


## 🏗️ Funcionalidades

- 📊 **Dashboard em tempo real** com dados de acionamentos por cômodo
- 🧠 **Previsão de consumo energético diário** usando Regressão Linear
- 🌍 **Simulação de sensores por cômodo** (Quarto1, Quarto2, Sala, Cozinha)
- 🎯 **Meta de consumo diário** com alertas de excesso
- 🔄 **Atualização automática do sistema** via `streamlit_autorefresh`
- 📉 **Clusterização de perfis de uso** com KMeans + PCA
- 🧾 **Exportação de relatórios em PDF**
- ☀️ **Comparativo com geração solar simulada**

---

## 🧪 Tecnologias Utilizadas

- `Python`
- `Pandas` e `NumPy` – tratamento e análise de dados
- `Scikit-learn` – regressão linear e KMeans
- `Matplotlib`, `Seaborn` e `Plotly` – visualizações
- `Streamlit` – dashboard interativo
- `FPDF` – geração de relatórios em PDF
- `Pillow` – imagens no dashboard

---

## 📁 Estrutura do Projeto

```bash
laguna_city_digital/
│
├── app.py                  # Aplicação principal Streamlit
├── consumo_model.pkl       # Modelo de previsão treinado
├── cluster_model.pkl       # Modelo KMeans treinado
├── dados/
│   └── Consumo_de_Energia_Analise.xlsx  # Dados simulados por cômodo
├── relatorios/
│   └── relatorio_consumo_YYYY-MM-DD.pdf
├── imagens/
│   ├── grafico_pca.png
│   ├── heatmap_cluster.png
│   └── grafico_regressao.png
└── README.md


## 📈 Exemplos de Visualizações

- ✅ **Clusterização com PCA**  
  Distribuição de padrões de uso por perfil energético

- 🔥 **Heatmap de acionamentos**  
  Percentual de uso por cômodo

- 📉 **Gráfico Real vs Previsto**  
  Avaliação do modelo de previsão

---

## 📊 Resultados do Modelo

- **R²**: 0.70  
- **MSE**: 11.528,06  
- **Cômodo com maior influência**: Sala (28.21%)

---

## 💡 Aplicações Finais

- Estabelecimento de **metas de consumo personalizadas**
- Geração de **alertas em tempo real**
- Apoio à **sustentabilidade energética urbana**
- Base para expansão em uma **Smart City completa**

---

## 🧑‍💻 Autor

**André Ribeiro**  
Contato: andreandson09@gmail.com

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License**.

> “Quem mede, controla. E quem controla, economiza.” 🌱

