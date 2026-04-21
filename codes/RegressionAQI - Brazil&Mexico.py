import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np  

# carregar os dados
df = pd.read_csv(
    r"C:\Users\jvsoa\OneDrive\Documents\Programação\Faculdade\Projeto Mexico X Portugues\datas\Database_pollution_aqi.csv",
    sep=';',          # separador do arquivo
    decimal=','       # decimal no formato brasileiro
)

# remover linhas com valores vazios nas colunas usadas
df = df.dropna(subset=[
    'Vehicles_Increase_%',
    'Industries_Increase_%',
    'CO2_Emissions_MT',
    'Green_Space_Ratio_%',
    'Population_Density_Per_SqKm',
    'AQI',
    'PM2.5',
    'PM10'
])

# remover valores fora do intervalo esperado
df = df[
    (df['AQI'] < 500) &
    (df['PM2.5'] < 500) &
    (df['PM10'] < 500) &
    (df['AQI'] > 0) &
    (df['PM2.5'] > 1) &
    (df['PM10'] > 0)
]

# cidades analisadas
cidades = ['Sao Paulo', 'Puebla']

for cidade in cidades:

    # filtrar os dados da cidade
    df_cidade = df[df['City'] == cidade]

    # definir variáveis
    X = df_cidade[['PM2.5', 'PM10']]
    y = df_cidade['AQI']

    # separar treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # treinar o modelo
    model = LinearRegression()
    model.fit(X_train, y_train)

    # mostrar resultados
    print(f"\n--- {cidade} ---")
    print("Intercepto:", model.intercept_)
    print("Coeficientes:", model.coef_)
    print("R² treino:", model.score(X_train, y_train))
    print("R² teste:", model.score(X_test, y_test))

    # gerar gráficos
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    # ===== PM2.5 =====
    axs[0].scatter(df_cidade['PM2.5'], df_cidade['AQI'])

    x_pm25 = np.linspace(df_cidade['PM2.5'].min(), df_cidade['PM2.5'].max(), 100)
    pm10_media = df_cidade['PM10'].mean()

    y_pm25 = model.intercept_ + model.coef_[0]*x_pm25 + model.coef_[1]*pm10_media

    axs[0].plot(x_pm25, y_pm25)
    axs[0].set_title(f'{cidade} - PM2.5 vs AQI')
    axs[0].plot(x_pm25, y_pm25, color='red')
    # ===== PM10 =====
    axs[1].scatter(df_cidade['PM10'], df_cidade['AQI'])

    x_pm10 = np.linspace(df_cidade['PM10'].min(), df_cidade['PM10'].max(), 100)
    pm25_media = df_cidade['PM2.5'].mean()

    y_pm10 = model.intercept_ + model.coef_[1]*x_pm10 + model.coef_[0]*pm25_media

    axs[1].plot(x_pm10, y_pm10)
    axs[1].set_title(f'{cidade} - PM10 vs AQI')
    axs[1].plot(x_pm10, y_pm10, color='red')

    plt.show()

    plt.show()