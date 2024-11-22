import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Crear datos de ejemplo para un mes
dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
n_samples = len(dates)

# Simular datos de producción minera
data = {
    'Fecha': dates,
    'Producción': np.random.normal(1000, 100, n_samples),
    'Ley_Cu': np.random.normal(2.5, 0.3, n_samples),
    'Recuperación': np.random.normal(85, 5, n_samples),
    'Costos': np.random.normal(50, 5, n_samples)
}

df = pd.DataFrame(data)

# Crear un dashboard más profesional
plt.style.use('dark_background')
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Dashboard de Control de Producción Minera', size=16, y=0.95)

# 1. Producción diaria
axes[0,0].plot(df['Fecha'], df['Producción'], 'g-', linewidth=2)
axes[0,0].fill_between(df['Fecha'], df['Producción'], alpha=0.2, color='green')
axes[0,0].set_title('Producción Diaria (ton)')
axes[0,0].set_xticklabels(df['Fecha'].dt.strftime('%d-%m'), rotation=45)
axes[0,0].grid(True, alpha=0.3)

# 2. Ley de Cobre
sns.boxplot(y=df['Ley_Cu'], ax=axes[0,1], color='yellow')
axes[0,1].set_title('Distribución de Ley de Cu (%)')
axes[0,1].grid(True, alpha=0.3)

# 3. Recuperación vs Ley
scatter = axes[1,0].scatter(df['Ley_Cu'], df['Recuperación'],
                          c=df['Producción'], cmap='viridis')
axes[1,0].set_title('Recuperación vs Ley')
axes[1,0].set_xlabel('Ley Cu (%)')
axes[1,0].set_ylabel('Recuperación (%)')
plt.colorbar(scatter, ax=axes[1,0], label='Producción (ton)')
axes[1,0].grid(True, alpha=0.3)

# 4. Costos Operativos
axes[1,1].plot(df['Fecha'], df['Costos'], 'r-', linewidth=2)
axes[1,1].fill_between(df['Fecha'], df['Costos'], alpha=0.2, color='red')
axes[1,1].set_title('Costos Operativos (USD/ton)')
axes[1,1].set_xticklabels(df['Fecha'].dt.strftime('%d-%m'), rotation=45)
axes[1,1].grid(True, alpha=0.3)

# Ajustar el diseño
plt.tight_layout()
plt.show()

# Crear un resumen estadístico
print("\nResumen Estadístico:")
print(df.describe().round(2))
