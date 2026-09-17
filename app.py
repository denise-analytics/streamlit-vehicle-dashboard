import pandas as pd
import plotly.express as px
import streamlit as st

# Título do app
st.header("Análise de anúncios de veículos")

# Ler o dataset
df = pd.read_csv("data/vehicles_us.csv")

# Mostrar os primeiros dados
st.write("Visualização inicial dos dados:")
st.dataframe(df.head())

# Checkbox para histograma
build_histogram = st.checkbox("Criar histograma do preço")

if build_histogram:
    st.write("Histograma dos preços dos veículos")
    fig_hist = px.histogram(df, x="price")
    st.plotly_chart(fig_hist, width="stretch")

# Checkbox para gráfico de dispersão
build_scatter = st.checkbox("Criar gráfico de dispersão (preço x odômetro)")

if build_scatter:
    st.write("Gráfico de dispersão: preço vs odômetro")
    fig_scatter = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig_scatter, width="stretch")

