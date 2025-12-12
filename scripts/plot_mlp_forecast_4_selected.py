import matplotlib.pyplot as plt

# Только 4 отобранных состава — в порядке таблицы 3.5
compositions = [
    'ChCl–ZnCl₂\n1:1,7',
    'ChCl–SnCl₂\n1:1,6',
    'ChCl–бетаин\n1:2,0',
    'ChCl–глицерин\n(контроль)'
]

forecast = [82.14, 85.62, 71.33, 68.79]

plt.figure(figsize=(10, 7))
bars = plt.bar(compositions, forecast, color='#3498db', edgecolor='black', linewidth=1.5, alpha=0.9)

plt.ylabel('Прогнозируемый выход коллагена, % (MLP)', fontsize=15)
plt.title('Рисунок 3.3. Прогнозируемый выход коллагена\nдля четырёх отобранных составов DES\n(MLP-модель, R² = 0.987, MAE = 1.78 %)', fontsize=16, pad=20)
plt.ylim(0, 100)
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Подписи над столбцами
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1.5,
             f'{height:.1f}%', ha='center', va='bottom', fontsize=14, fontweight='bold')

plt.xticks(rotation=0, fontsize=13)
plt.tight_layout()
plt.savefig("/project/results/Рисунок_3.3_Прогноз_MLP_4_состава.png", dpi=400, bbox_inches='tight')
plt.close()

print("ГОТОВО! Чистый прогноз MLP только для 4 отобранных составов — рисунок 3.3 создан")
