#ESPANHOS
# 📊 Análisis de AQI - São Paulo vs Puebla

Proyecto de análisis de la calidad del aire comparando São Paulo (Brasil) y Puebla (México), utilizando modelos de regresión para evaluar el impacto de partículas y factores urbanos en el AQI.

---

## 🎯 Objetivo

Analizar el impacto de las partículas **PM2.5** y **PM10** en el índice de calidad del aire (**AQI**) y comparar su comportamiento entre dos ciudades con contextos distintos.

Además, se busca diferenciar entre:

- **Factores directos** → partículas (PM2.5, PM10)  
- **Factores indirectos** → variables urbanas (CO₂, vehículos, densidad, etc.)

---

## 🌫️ ¿Qué son PM2.5 y PM10?

- **PM2.5**: partículas muy finas (≤ 2,5 µm), capaces de penetrar profundamente en los pulmones  
- **PM10**: partículas más grandes (≤ 10 µm), afectan principalmente las vías respiratorias  

Estas partículas son determinantes en el cálculo del AQI.

---

## 🧹 Tratamiento de los datos

Se aplicaron las siguientes etapas:

- Eliminación de valores nulos  
- Filtrado de valores fuera del rango:
  - AQI > 500  
  - PM2.5 > 500  
  - PM10 > 500  
  - valores negativos  
- Estandarización de la lectura del CSV  

---

## ⚙️ Metodología

Se desarrollaron tres modelos de regresión:

- **Modelo 1 – Directo (Poluentes)**  
  - PM2.5, PM10 → AQI  

- **Modelo 2 – Indirecto (Urbano)**  
  - CO2, vehículos, industria, densidad poblacional, áreas verdes → AQI  

- **Modelo 3 – Completo (Híbrido)**  
  - Combinación de todas las variables  

División de datos:

- 80% entrenamiento  
- 20% prueba  

---

## 📈 Resultados

### 📍 Modelo 1 – Poluentes
- R² ≈ 0.86 – 0.87  
- Alta capacidad explicativa  

### 📍 Modelo 2 – Urbano
- R² ≈ 0.40 – 0.50  
- Capacidad limitada  

### 📍 Modelo 3 – Completo
- R² ≈ 0.87 – 0.88  
- Leve mejora predictiva  

---

## 🔍 Interpretación

- Existe una relación directa fuerte entre partículas y AQI  
- PM2.5 presenta mayor impacto relativo que PM10  
- Variables urbanas actúan como factores indirectos  
- El comportamiento es consistente entre ambas ciudades  

---

## 💡 Insight principal

> La calidad del aire no está determinada directamente por factores urbanos, sino por la concentración de partículas, que son consecuencia de estos factores.

---

## 📊 Visualización

Se generaron gráficos para analizar:

- PM2.5 vs AQI  
- PM10 vs AQI  
- Matriz de correlación entre variables  

---

## 🚀 Tecnologías utilizadas

- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  
- Seaborn  

---

## 📁 Estructura del proyecto

📂 proyecto-aqi  
├── data/  
├── codigo/  
├── graficos/  
├── README.md  
└── analisis.pdf  

---

## 📌 Posibles mejoras

- Modelos en múltiples etapas (urbano → partículas → AQI)  
- Modelos no lineales (Random Forest, etc.)  
- Análisis temporal  
- Expansión geográfica  

---

## 🤝 Proyecto colaborativo

#PORTUGUES
Proyecto desarrollado en colaboración entre Brasil y México.
# 📊 Análise de AQI - São Paulo vs Puebla

Projeto de análise da qualidade do ar comparando São Paulo (Brasil) e Puebla (México), utilizando modelos de regressão para avaliar o impacto de partículas e fatores urbanos no AQI.

---

## 🎯 Objetivo

Analisar o impacto das partículas **PM2.5** e **PM10** no índice de qualidade do ar (**AQI**) e comparar seu comportamento entre duas cidades com contextos distintos.

Além disso, busca-se diferenciar entre:

- **Fatores diretos** → partículas (PM2.5, PM10)  
- **Fatores indiretos** → variáveis urbanas (CO₂, veículos, densidade, etc.)

---

## 🌫️ O que são PM2.5 e PM10?

- **PM2.5**: partículas muito finas (≤ 2,5 µm), capazes de penetrar profundamente nos pulmões  
- **PM10**: partículas maiores (≤ 10 µm), afetam principalmente as vias respiratórias  

Essas partículas são determinantes no cálculo do AQI.

---

## 🧹 Tratamento dos dados

Foram aplicadas as seguintes etapas:

- Remoção de valores nulos  
- Filtragem de valores fora do padrão:
  - AQI > 500  
  - PM2.5 > 500  
  - PM10 > 500  
  - valores negativos  
- Padronização da leitura do CSV  

---

## ⚙️ Metodologia

Foram desenvolvidos três modelos de regressão:

- **Modelo 1 – Direto (Poluentes)**  
  - PM2.5, PM10 → AQI  

- **Modelo 2 – Indireto (Urbano)**  
  - CO2, veículos, indústria, densidade populacional, áreas verdes → AQI  

- **Modelo 3 – Completo (Híbrido)**  
  - Combinação de todas as variáveis  

Divisão dos dados:

- 80% treino  
- 20% teste  

---

## 📈 Resultados

### 📍 Modelo 1 – Poluentes
- R² ≈ 0.86 – 0.87  
- Alto poder explicativo  

### 📍 Modelo 2 – Urbano
- R² ≈ 0.40 – 0.50  
- Baixa capacidade explicativa  

### 📍 Modelo 3 – Completo
- R² ≈ 0.87 – 0.88  
- Leve ganho preditivo  

---

## 🔍 Interpretação

- Existe uma relação direta forte entre partículas e AQI  
- PM2.5 apresenta maior impacto relativo que PM10  
- Variáveis urbanas atuam como fatores indiretos  
- O comportamento é consistente entre as cidades  

---

## 💡 Insight principal

> A qualidade do ar não é diretamente determinada por fatores urbanos, mas sim pela concentração de partículas, que são consequência desses fatores.

---

## 📊 Visualização

Foram gerados gráficos para análise de:

- PM2.5 vs AQI  
- PM10 vs AQI  
- Matriz de correlação entre variáveis  

---

## 🚀 Tecnologias utilizadas

- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  
- Seaborn  

---

## 📁 Estrutura do projeto

📂 projeto-aqi  
├── data/  
├── codigo/  
├── graficos/  
├── README.md  
└── analise.pdf  

---

## 📌 Possíveis melhorias

- Modelagem em múltiplas etapas (urbano → partículas → AQI)  
- Modelos não lineares  
- Análise temporal  
- Expansão para outras cidades  

---

## 🤝 Projeto colaborativo

Projeto desenvolvido em colaboração entre Brasil e México.
