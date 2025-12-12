import matplotlib.pyplot as plt
import numpy as np

# Данные из твоей таблицы 3.5
compositions = [
    'ChCl–ZnCl₂\n1:1,7',
    'ChCl–SnCl₂\n1:1,6',
    'ChCl–бетаин\n1:2,0',
    'ChCl–глицерин\n(контроль)'
]

predicted = [82.14, 85.62, 71.33, 68.79]
experimental = [84.8, 83.9, 82.5, 77.4]
error = [2.1, 2.0, 2.4, 2.8]  # стандартное отклонение

x = np.arange(len(compositions))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, predicted, width, label='Прогноз MLP-модели', color='#3498db', alpha=0.8)
bars2 = ax.bar(x + width/2, experimental, width, label='Эксперимент (n=9)', color='#27ae60', yerr=error, capsize=5, alpha=0.9)

ax.set_ylabel('Выход коллагена, %', fontsize=14)
ax.set_title('Рисунок 3.3 — Сравнение прогнозируемого и экспериментального выхода коллагена\nдля четырёх отобранных составов DES', fontsize=15, pad=20)
ax.set_xticks(x)
ax.set_xticklabels(compositions, fontsize=12)
ax.legend(fontsize=12)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Подписи значений над столбцами
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{height:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.ylim(0, 95)
plt.tight_layout()
plt.savefig("/project/results/Рисунок_3.3_Сравнение_прогноз_эксперимент.png", dpi=400, bbox_inches='tight')
plt.close()

print("ГОТОВО! Рисунок 3.3 создан:")
print("   → results/Рисунок_3.3_Сравнение_прогноз_эксперимент.png")
