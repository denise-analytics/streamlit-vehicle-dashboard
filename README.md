## 🚗 Dashboard Interativo – Anúncios de Veículos Usados  
**Sprint 5 | Data Analytics & Web App**

### 🔎 Visão Geral  
Este projeto consiste no desenvolvimento de um **dashboard interativo em Streamlit** para análise exploratória de **anúncios de veículos usados** nos Estados Unidos.

O foco principal do projeto é a **criação, implantação e disponibilização pública de um aplicativo web**, aplicando boas práticas de desenvolvimento de software e visualização de dados, conforme proposto no Sprint 5 da formação em Análise de Dados.

---

### 📸 Visualização do Aplicativo  

**Visão geral do dashboard**
![Visão geral do dashboard](app_dashboard.png)

**Gráfico de dispersão – Preço vs Odômetro**
![Gráfico de dispersão: preço vs odômetro](scatter_preco_odometro.png)

---

### 🎯 Objetivo do Projeto  
Criar um aplicativo web que permita explorar dados de anúncios de veículos de forma simples e interativa, possibilitando responder perguntas como:

- Como a quilometragem dos veículos está distribuída?
- Qual a relação entre quilometragem e preço?
- Quais padrões gerais podem ser observados nos anúncios?

O aplicativo transforma dados brutos em **visualizações acessíveis**, apoiando análises iniciais e entendimento do mercado de veículos usados.

---

### 🗂️ Dados Utilizados  
- Dataset: **vehicles_us.csv**
- Fonte: conjunto de dados educacional fornecido para o projeto
- Contém informações sobre anúncios de veículos usados

**Principais colunas:**
- `price` – preço do veículo  
- `odometer` – quilometragem  
- `model_year` – ano do modelo  
- `condition` – condição do veículo  
- `fuel`, `transmission`, `type` – características do veículo  

---

### 🛠️ Tecnologias e Ferramentas  
- **Python**
- **pandas** – manipulação e preparação dos dados  
- **plotly-express** – visualizações interativas  
- **Streamlit** – desenvolvimento do aplicativo web  
- **Jupyter Notebook** – análise exploratória (EDA)  
- **Git & GitHub** – versionamento  
- **Render** – implantação do aplicativo em nuvem  

---

### 🔄 Etapas do Projeto  
1. Configuração do ambiente virtual Python  
2. Análise exploratória inicial dos dados (EDA) em notebook  
3. Tratamento básico dos dados para visualização  
4. Desenvolvimento do aplicativo web com Streamlit  
5. Criação de gráficos interativos:
   - Histograma da distribuição de preços  
   - Gráfico de dispersão entre preço e quilometragem  
6. Implantação do aplicativo na nuvem utilizando o Render  

---

### 📊 Funcionalidades do Aplicativo  
O dashboard permite ao usuário:

- Visualizar a distribuição dos preços dos veículos  
- Analisar a relação entre preço e quilometragem  
- Interagir com gráficos por meio de caixas de seleção  
- Explorar os dados diretamente no navegador, sem necessidade de código  

📌 O foco do aplicativo é **exploração visual e interatividade**, e não modelagem avançada.

---

### 🌐 Aplicação Online  
🔗 **Link do aplicativo:**  
👉 https://sprint5-streamlit.onrender.com/

> Observação: como o aplicativo está hospedado em um plano gratuito, pode levar alguns minutos para “acordar” após períodos de inatividade.

---

### ▶️ Como Executar o Projeto Localmente  

```bash
git clone https://github.com/denise-analytics/sprint5_streamlit
cd sprint5_streamlit
pip install -r requirements.txt
streamlit run app.py


