#ESPANHOL
# 📊 Análisis de AQI - São Paulo vs Puebla

Proyecto de análisis de la calidad del aire comparando São Paulo (Brasil) y Puebla (México), utilizando regresión lineal para evaluar el impacto de PM2.5 y PM10 en el AQI.

---

## 🎯 Objetivo

Analizar cómo las partículas **PM2.5** y **PM10** influyen en el índice de calidad del aire (**AQI**) y comparar el comportamiento entre dos ciudades de distintos países.

---

## 🌫️ ¿Qué son PM2.5 y PM10?

- **PM2.5**: partículas muy finas (≤ 2,5 µm), pueden penetrar profundamente en los pulmones  
- **PM10**: partículas más grandes (≤ 10 µm), afectan principalmente las vías respiratorias  

Estas partículas se utilizan directamente en el cálculo del AQI.

---

## 🧹 Tratamiento de los datos

Se aplicaron los siguientes pasos:

- Eliminación de valores nulos  
- Filtrado de valores fuera del rango:
  - AQI > 500  
  - PM2.5 > 500  
  - PM10 > 500  
  - valores negativos  
- Estandarización de la lectura del archivo CSV  

---

## ⚙️ Metodología

- Modelo: **Regresión Lineal**
- Variables independientes:
  - PM2.5
  - PM10
- Variable dependiente:
  - AQI
- División:
  - 80% entrenamiento
  - 20% prueba

---

## 📈 Resultados

### 📍 São Paulo
- R² ≈ 0.86  
- PM2.5 ≈ 0.68  
- PM10 ≈ 0.54  

### 📍 Puebla
- R² ≈ 0.87  
- PM2.5 ≈ 0.65  
- PM10 ≈ 0.53  

---

## 🔍 Interpretación

- Existe una relación lineal positiva entre PM y AQI  
- PM2.5 presenta un impacto ligeramente mayor que PM10  
- El comportamiento es consistente entre ambas ciudades  

---

## 💡 Insight principal

> El aumento de la concentración de partículas en el aire está directamente asociado al empeoramiento de la calidad del aire, independientemente de la ciudad analizada.

---

## 📊 Visualización

Los gráficos muestran la relación entre:

- PM2.5 vs AQI  
- PM10 vs AQI  

con la línea de regresión representando el modelo.

---

## 🚀 Tecnologías utilizadas

- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  

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

- Incluir más variables (CO2, vehículos, etc.)  
- Probar modelos más avanzados  
- Análisis temporal de los datos  

---

## 🤝 Proyecto colaborativo

Proyecto desarrollado en colaboración entre Brasil y México, utilizando datos de la ciudad de Puebla.

#PORTUGUES
# 📊 Análise de AQI - São Paulo vs Puebla

Projeto de análise da qualidade do ar comparando São Paulo (Brasil) e Puebla (México), utilizando regressão linear para avaliar o impacto de PM2.5 e PM10 no AQI.

---

## 🎯 Objetivo

Analisar como as partículas **PM2.5** e **PM10** influenciam o índice de qualidade do ar (**AQI**) e comparar o comportamento entre duas cidades de países diferentes.

---

## 🌫️ O que são PM2.5 e PM10?

- **PM2.5**: partículas muito finas (≤ 2,5 µm), conseguem penetrar profundamente nos pulmões  
- **PM10**: partículas maiores (≤ 10 µm), afetam principalmente as vias respiratórias  

Essas partículas são utilizadas diretamente no cálculo do AQI.

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

- Modelo: **Regressão Linear**
- Variáveis independentes:
  - PM2.5
  - PM10
- Variável dependente:
  - AQI
- Divisão:
  - 80% treino
  - 20% teste

---

## 📈 Resultados

### 📍 São Paulo
- R² ≈ 0.86  
- PM2.5 ≈ 0.68  
- PM10 ≈ 0.54  

### 📍 Puebla
- R² ≈ 0.87  
- PM2.5 ≈ 0.65  
- PM10 ≈ 0.53  

---

## 🔍 Interpretação

- Existe uma relação linear positiva entre PM e AQI  
- PM2.5 apresenta impacto levemente maior que PM10  
- O comportamento é consistente entre as duas cidades  

---

## 💡 Insight principal

> O aumento da concentração de partículas no ar está diretamente associado à piora da qualidade do ar, independentemente da cidade analisada.

---

## 📊 Visualização

Os gráficos mostram a relação entre:

- PM2.5 vs AQI  
- PM10 vs AQI  

com linha de regressão representando o modelo.

---

## 🚀 Tecnologias utilizadas

- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  

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

- Incluir mais variáveis (CO2, veículos, etc.)
- Testar modelos mais avançados
- Análise temporal dos dados

---

## 🤝 Projeto colaborativo

Projeto desenvolvido em colaboração entre Brasil e México, utilizando dados da cidade de Puebla.
