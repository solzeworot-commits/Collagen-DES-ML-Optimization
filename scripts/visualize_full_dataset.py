import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Загружаем датасет (он уже должен быть в results, если запускал генерацию)
df = pd.read_csv("/project/results/simulated_DES_collagen_dataset_1240.csv")

# 1. 3D-скаттер: выход от температуры и pH, цвет — концентрация DES
fig = plt.figure(figsize=(12,9))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(df['Температура'], df['pH'], df['Выход коллагена, %'], 
                c=df['Концентрация DES, %'], cmap='viridis', s=30, alpha=0.7)
ax.set_xlabel('Температура, °C')
ax.set_ylabel('pH')
ax.set_zlabel('Выход коллагена, %')
ax.set_title('3D-визуализация симулированного датасета (n=1240)\nВыход коллагена от температуры и pH (цвет — концентрация DES)')
plt.colorbar(sc, label='Концентрация DES, %')
plt.tight_layout()
plt.savefig("/project/results/Визуализация_датасета_3D_выход_от_темп_pH.png", dpi=400)
plt.close()

# 2. Heatmap: средний выход по соотношению и температуре
pivot = df.pivot_table(values='Выход коллагена, %', index='Молярное соотношение', columns='Температура', aggfunc='mean')
plt.figure(figsize=(12,8))
sns.heatmap(pivot, annot=False, cmap='YlGnBu', cbar_kws={'label': 'Выход коллагена, %'})
plt.title('Heatmap: средний выход коллагена по соотношению и температуре\n(симулированный датасет, n=1240)')
plt.xlabel('Температура, °C')
plt.ylabel('Молярное соотношение HBA:HBD')
plt.tight_layout()
plt.savefig("/project/results/Визуализация_датасета_Heatmap_соотношение_температура.png", dpi=400)
plt.close()

# 3. Pairplot ключевых параметров
sns.set_style("whitegrid")
pair = sns.pairplot(df[['Температура', 'pH', 'Концентрация DES, %', 'Выход коллагена, %']], 
                    diag_kind='kde', plot_kws={'alpha':0.6})
pair.fig.suptitle('Pairplot ключевых параметров симулированного датасета (n=1240)', y=1.02, fontsize=16)
plt.tight_layout()
plt.savefig("/project/results/Визуализация_датасета_Pairplot_ключевые_параметры.png", dpi=400)
plt.close()

# 4. Histogram распределения выхода с нормативом
plt.figure(figsize=(10,6))
plt.hist(df['Выход коллагена, %'], bins=50, color='#27ae60', edgecolor='black', alpha=0.8)
plt.axvline(x=85, color='red', linestyle='--', linewidth=3, label='Норматив ≥85 % (ТР ТС 021/2011)')
plt.xlabel('Выход коллагена, %', fontsize=14)
plt.ylabel('Частота', fontsize=14)
plt.title('Распределение прогнозируемого выхода коллагена\n(симулированный датасет, n=1240)', fontsize=16)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("/project/results/Визуализация_датасета_Histogram_выхода.png", dpi=400)
plt.close()

print("ГОТОВО! 4 завораживающих визуализации датасета созданы:")
print("   • 3D_выход_от_темп_pH.png")
print("   • Heatmap_соотношение_температура.png")
print("   • Pairplot_ключевые_параметры.png")
print("   • Histogram_выхода.png")
