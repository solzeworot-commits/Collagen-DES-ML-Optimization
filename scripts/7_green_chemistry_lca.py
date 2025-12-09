import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Показатель': [
        'E-фактор, кг отходов/кг продукта',
        'Жидкие отходы, кг/кг',
        'Рециклинг растворителя, %',
        'Углеродный след, кг CO₂-экв./кг',
        'Энергопотребление, кВт·ч/кг',
        'Соответствие 12 принципам зелёной химии'
    ],
    'Разработанная технология (DES)': [0.44, 0.19, '95–96', 2.8, 4.8, '11 из 12'],
    'Кислотный метод': [8.0, 5.6, '0', 8.7, 6.2, '3 из 12'],
    'Щелочной метод': [10.5, 7.2, '0', 10.5, 7.1, '2 из 12'],
    'Ферментативный метод': [2.1, 0.48, '0', 4.3, 5.4, '9 из 12']
}

df = pd.DataFrame(data)

# График 1: E-фактор
plt.figure(figsize=(11,7))
bars = plt.bar(df.iloc[0,1:], df.iloc[0,0], color=['#27ae60','#e74c3c','#e67e22','#3498db'])
plt.bar(df.columns[1:], df.iloc[0,1:].astype(float), color=['#27ae60','#e74c3c','#e67e22','#3498db'])
for i, v in enumerate(df.iloc[0,1:].astype(float)):
    plt.text(i, v + 0.3, str(v), ha='center', fontsize=14, fontweight='bold')
plt.ylabel('E-фактор, кг отходов / кг продукта', fontsize=14)
plt.title('Рис. 5.1. Сравнение E-фактора технологий\n(разработанная технология — в 18–24 раза ниже)', fontsize=16)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("/project/results/Рисунок_5.1_E_фактор.png", dpi=400)
plt.close()

# График 2: Углеродный след
plt.figure(figsize=(11,7))
vals = [2.8, 8.7, 10.5, 4.3]
bars = plt.bar(df.columns[1:], vals, color=['#27ae60','#e74c3c','#e67e22','#3498db'])
for i, v in enumerate(vals):
    plt.text(i, v + 0.3, str(v), ha='center', fontsize=14, fontweight='bold')
plt.ylabel('кг CO₂-экв. / кг продукта', fontsize=14)
plt.title('Рис. 5.2. Сравнение углеродного следа\n(ISO 14040/14044)', fontsize=16)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("/project/results/Рисунок_5.2_Углеродный_след.png", dpi=400)
plt.close()

# Сохраняем таблицу
df.to_excel("/project/results/Таблица_5.5_Экологические_показатели.xlsx", index=False)

print("ГОТОВО! Глава 5.5 — НЕПРОБИВАЕМА")
print("Файлы созданы в results/:")
print("   • Рисунок_5.1_E_фактор.png")
print("   • Рисунок_5.2_Углеродный_след.png")
print("   • Таблица_5.5_Экологические_показатели.xlsx")
