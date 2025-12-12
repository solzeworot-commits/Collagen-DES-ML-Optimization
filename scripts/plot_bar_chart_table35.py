import pandas as pd
import matplotlib.pyplot as plt

# Твои данные из таблицы 3.5
data = {
    'Состав DES': [
        'ChCl–ZnCl₂\n1:1,7',
        'ChCl–SnCl₂\n1:1,6',
        'ChCl–бетаин\n1:2,0',
        'ChCl–глицерин\n(контроль)'
    ],
    'Прогноз MLP, %': [82.14, 85.62, 71.33, 68.79],
    'Эксперимент, %': [84.8, 83.9, 82.5, 77.4],
    'Ошибка, %': [2.1, 2.0, 2.4, 2.8]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 7))

x = range(len(df))
width = 0.35

bars1 = ax.bar([i - width/2 for i in x], df['Прогноз MLP, %'], width, label='Прогноз MLP', color='#3498db', edgecolor='black')
bars2 = ax.bar([i + width/2 for i in x], df['Эксперимент, %'], width, label='Эксперимент (n=9)', color='#27ae60', edgecolor='black', yerr=df['Ошибка, %'], capsize=8)

ax.set_ylabel('Выход коллагена, %', fontsize=14)
ax.set_title('Рисунок 3.3. Сравнение прогнозируемого и экспериментального выхода коллагена\nдля четырёх отобранных составов DES', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(df['Состав DES'], fontsize=12, rotation=0, ha='center')
ax.legend(fontsize=12)
ax.grid(axis='y', alpha=0.3)

# Подписи значений над столбцами
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{height:.1f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig("/project/results/Рисунок_3.3_Сравнение_прогноз_эксперимент.png", dpi=400, bbox_inches='tight')
plt.close()

print("ГОТОВО! Рисунок 3.3 создан — идеальный для диссертации")
