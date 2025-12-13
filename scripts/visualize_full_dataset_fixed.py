import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Загружаем датасет
df = pd.read_csv("/project/results/simulated_DES_collagen_dataset_1240.csv")

# Переименуем ключевые столбцы для удобства (если нужно)
df.rename(columns={
    'Temperature': 'Температура',
    'pH': 'pH',
    'Concentration_DES_%': 'Концентрация DES, %',
    'Yield_collagen_%': 'Выход коллагена, %',
    'Molar_ratio': 'Молярное соотношение'
}, inplace=True)

# 1. 3D-скаттер
fig = plt.figure(figsize=(12,9))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(df['Температура'], df['pH'], df['Выход коллагена, %'], 
                c=df['Концентрация DES, %'], cmap='viridis', s=30, alpha=0.7)
ax.set_xlabel('Температура, °C')
ax.set_ylabel('pH')
ax.set_zlabel('Выход коллагена, %')
ax.set_title('3D-визуализация симулированного датасета (n=1240)\nВыход коллагена от температуры и pH')
plt.colorbar(sc, label='Концентрация DES, %')
plt.tight_layout()
plt.savefig("/project/results/Визуализация_датасета_3D.png", dpi=400)
plt.close()

# 2. Heatmap
pivot = df.pivot_table(values='Выход коллагена, %', index='Молярное соотношение', columns='Температура', aggfunc='mean')
plt.figure(figsize=(12,8))
sns.heatmap(pivot, annot=False, cmap='YlGnBu', cbar_kws={'label': 'Выход коллагена, %'})
plt.title('Heatmap: средний выход коллагена по соотношению и температуре (n=1240)')
plt.xlabel('Температура, °C')
plt.ylabel('Молярное соотношение')
plt.tight_layout()
plt.savefig("/project/results/Визуализация_датасета_Heatmap.png", dpi=400)
plt.close()

# 3. Pairplot
sns.pairplot(df[['Температура', 'pH', 'Концентрация DES, %', 'Выход коллагена, %']], 
             diag_kind='kde', plot_kws={'alpha':0.6})
plt.suptitle('Pairplot ключевых параметров симулированного датасета (n=1240)', y=1.02)
plt.tight_layout()
plt.savefig("/project/results/Визуализация_датасета_Pairplot.png", dpi=400)
plt.close()

# 4. Histogram
plt.figure(figsize=(10,6))
plt.hist(df['Выход коллагена, %'], bins=50, color='#27ae60', edgecolor='black', alpha=0.8)
plt.axvline(x=85, color='red', linestyle='--', linewidth=3, label='Норматив ≥85 %')
plt.xlabel('Выход коллагена, %')
plt.ylabel('Частота')
plt.title('Распределение прогнозируемого выхода коллагена (n=1240)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("/project/results/Визуализация_датасета_Histogram.png", dpi=400)
plt.close()

print("ГОТОВО! 4 завораживающих графика созданы в results/")
