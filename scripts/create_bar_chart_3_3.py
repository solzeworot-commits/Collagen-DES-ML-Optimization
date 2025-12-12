import matplotlib.pyplot as plt
import numpy as np

# Данные из твоей таблицы 3.5 (реальные!)
compositions = [
    'ChCl–ZnCl₂\n1:1,7',
    'ChCl–SnCl₂\n1:1,6', 
    'Бетаин–лимонная\nкислота 1:1,1',
    'ChCl–глицерин\n(контроль) 1:2,0'
]

predicted = [84.8, 84.0, 80.8, 77.4]
experimental = [84.7, 83.9, 82.5, 77.4]

x = np.arange(len(compositions))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, predicted, width, label='Прогноз MLP', color='#3498db', edgecolor='black')
bars2 = ax.bar(x + width/2, experimental, width, label='Эксперимент (n=9)', color='#2ecc71', edgecolor='black', alpha=0.9)

ax.set_ylabel('Выход коллагена, %', fontsize=14)
ax.set_title('Рисунок 3.3. Сравнение прогнозируемого и экспериментального выхода коллагена\nдля четырёх отобранных составов DES', fontsize=16, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(compositions, fontsize=11, rotation=0, ha='center')
ax.legend(fontsize=12)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Подписи значений над столбцами
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{height}', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig("/project/results/Рисунок_3.3_Сравнение_прогноз_эксперимент.png", dpi=400, bbox_inches='tight')
plt.close()

print("ГОТОВО! Рисунок 3.3 создан — идеальный для диссертации")
