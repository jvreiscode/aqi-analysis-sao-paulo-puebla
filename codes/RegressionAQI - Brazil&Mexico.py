import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# carregar os dados
df = pd.read_csv(
    r"C:\Users\jvsoa\OneDrive\Documents\Programação\Faculdade\Projeto Mexico X Portugues\datas\Database_pollution_aqi.csv",
    sep=';',
    decimal=',',
    low_memory=False
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

def treinar_modelo(nome, X, y, escalar=False):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    if escalar:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
    else:
        scaler = None

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"\n===== {nome} =====")
    print("Intercepto:", model.intercept_)
    print("Coeficientes:", model.coef_)
    print("R² treino:", model.score(X_train, y_train))
    print("R² teste:", r2_score(y_test, y_pred))
    print("RMSE:", rmse)

    return {
        "modelo": model,
        "scaler": scaler,
        "r2": r2_score(y_test, y_pred),
        "rmse": rmse
    }

for cidade in cidades:
    print(f"\n\n==================== {cidade} ====================")

    # filtrar os dados da cidade
    df_cidade = df[df['City'] == cidade]

    y = df_cidade['AQI']

    # Modelo 1 - Direto (Poluentes)
    X1 = df_cidade[['PM2.5', 'PM10']]
    resultado1 = treinar_modelo("Modelo 1 - Direto (Poluentes)", X1, y, escalar=False)
    
    # Modelo 2 - Indireto (Urbano)
    X2 = df_cidade[
        [
            'Vehicles_Increase_%',
            'Industries_Increase_%',
            'CO2_Emissions_MT',
            'Green_Space_Ratio_%',
            'Population_Density_Per_SqKm'
        ]
    ]
    resultado2 = treinar_modelo("Modelo 2 - Indireto (Urbano)", X2, y, escalar=True)

    # Modelo 3 - Completo (Híbrido)
    X3 = df_cidade[
        [
            'PM2.5',
            'PM10',
            'Vehicles_Increase_%',
            'Industries_Increase_%',
            'CO2_Emissions_MT',
            'Green_Space_Ratio_%',
            'Population_Density_Per_SqKm'
        ]
    ]
    resultado3 = treinar_modelo("Modelo 3 - Completo (Híbrido)", X3, y, escalar=True)

    # Comparação final
    print("\n==================== COMPARAÇÃO FINAL ====================")
    print("Modelo 1 -> R²:", resultado1["r2"], "| RMSE:", resultado1["rmse"])
    print("Modelo 2 -> R²:", resultado2["r2"], "| RMSE:", resultado2["rmse"])
    print("Modelo 3 -> R²:", resultado3["r2"], "| RMSE:", resultado3["rmse"])

    # Gráficos - Modelo 1
    model = resultado1["modelo"]

    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    # Graficos sobre PM2.5
    axs[0].scatter(df_cidade['PM2.5'], df_cidade['AQI'], alpha=0.7)
    x_pm25 = np.linspace(df_cidade['PM2.5'].min(), df_cidade['PM2.5'].max(), 100)
    pm10_media = df_cidade['PM10'].mean()
    y_pm25 = model.intercept_ + model.coef_[0] * x_pm25 + model.coef_[1] * pm10_media
    axs[0].plot(x_pm25, y_pm25, color='red')
    axs[0].set_title(f'{cidade} - PM2.5 vs AQI')
    axs[0].set_xlabel('PM2.5')
    axs[0].set_ylabel('AQI')

    # Graficos sobre PM10
    axs[1].scatter(df_cidade['PM10'], df_cidade['AQI'], alpha=0.7)
    x_pm10 = np.linspace(df_cidade['PM10'].min(), df_cidade['PM10'].max(), 100)
    pm25_media = df_cidade['PM2.5'].mean()
    y_pm10 = model.intercept_ + model.coef_[1] * x_pm10 + model.coef_[0] * pm25_media
    axs[1].plot(x_pm10, y_pm10, color='red')
    axs[1].set_title(f'{cidade} - PM10 vs AQI')
    axs[1].set_xlabel('PM10')
    axs[1].set_ylabel('AQI')

    plt.tight_layout()
    plt.show()

    # Correlação
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_cidade.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title(f"Correlação entre variáveis - {cidade}")
    plt.tight_layout()
    plt.show()

    # VIF - Modelo 3
    print("\n==================== VIF (Multicolinearidade) ====================")
    X_vif = X3.copy()
    X_vif["intercept"] = 1

    vif_data = pd.DataFrame()
    vif_data["Variável"] = X_vif.columns
    vif_data["VIF"] = [
        variance_inflation_factor(X_vif.values, i)
        for i in range(X_vif.shape[1])
    ]
    print(vif_data)
