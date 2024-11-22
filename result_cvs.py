import pandas as pd
import numpy as np
from datetime import datetime

# Crear el rango de fechas (usando 'h' en lugar de 'H')
dates = pd.date_range(start='2024-01-01', end='2024-03-31', freq='h')

# Generar datos simulados
np.random.seed(42)  # Para reproducibilidad

# Número de muestras
n_samples = len(dates)

# Generar clasificaciones con distribución realista
clasificaciones = np.random.choice(
    ['Baja Ley', 'Media Ley', 'Alta Ley'],
    size=n_samples,
    p=[0.01, 0.44, 0.55]  # Probabilidades ajustadas según tus datos
)

# Generar datos para cada característica
data = {
    'Fecha': dates,
    'Clasificación': clasificaciones,
    'Tonelaje': np.random.normal(1000, 150, n_samples),
    'Ley_Cu': np.random.normal(1.5, 0.3, n_samples),
    'Recuperación': np.random.normal(85, 5, n_samples),
    'Humedad': np.random.normal(8, 1, n_samples),
    'Consumo_Energía': np.random.normal(500, 100, n_samples)
}

# Crear DataFrame
df = pd.DataFrame(data)

# Mostrar resumen estadístico
print("Resumen Estadístico por Clasificación:")
summary = df.groupby('Clasificación')[['Tonelaje', 'Ley_Cu', 'Recuperación', 'Humedad', 'Consumo_Energía']].describe().round(2)
print(summary)

# Guardar el DataFrame en un archivo CSV (usando una ruta local)
try:
    # Intentar guardar en el directorio actual
    df.to_csv('datos_mineral_3meses.csv', index=False)
    print("\nArchivo CSV guardado exitosamente como 'datos_mineral_3meses.csv'")
except Exception as e:
    print(f"\nError al guardar el archivo: {e}")

# Mostrar las primeras filas del DataFrame
print("\nPrimeras filas del DataFrame:")
print(df.head())

# Visualizar algunas métricas
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Gráfico de cajas para Tonelaje por Clasificación
df.boxplot(column='Tonelaje', by='Clasificación', ax=axes[0,0])
axes[0,0].set_title('Tonelaje por Clasificación')
axes[0,0].set_ylabel('Tonelaje')

# Gráfico de cajas para Ley_Cu por Clasificación
df.boxplot(column='Ley_Cu', by='Clasificación', ax=axes[0,1])
axes[0,1].set_title('Ley de Cobre por Clasificación')
axes[0,1].set_ylabel('Ley Cu (%)')

# Gráfico de cajas para Recuperación por Clasificación
df.boxplot(column='Recuperación', by='Clasificación', ax=axes[1,0])
axes[1,0].set_title('Recuperación por Clasificación')
axes[1,0].set_ylabel('Recuperación (%)')

# Gráfico de cajas para Consumo_Energía por Clasificación
df.boxplot(column='Consumo_Energía', by='Clasificación', ax=axes[1,1])
axes[1,1].set_title('Consumo de Energía por Clasificación')
axes[1,1].set_ylabel('Consumo Energía (kWh)')

plt.tight_layout()
plt.show()