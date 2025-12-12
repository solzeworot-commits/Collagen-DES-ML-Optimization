import matplotlib.pyplot as plt

# Твои 12 составов из таблицы 3.4 — только прогноз MLP
compositions = [
    'ChCl–ZnCl₂\n1:1,7',
    'ChCl–SnCl₂\n1:1,6',
    'ChCl–бетаин\n1:2,0',
    'ChCl–глицерин\n(контроль)',
    'Бетаин–глицерин\n1:2',
    'L-пролин–глицерин\n1:2',
    'Глюкоза–глицерин\n1:1,71',
    'ChCl–лимонная кислота\n1:1,5',
    'Бетаин–сорбит\n1:2',
    'Глицин–глицерин\n1:2',
    'ChCl–мочевина\n1:2',
    'Глюкоза–ментол\n1:1,2'
]

forecast = [82.14, 85.62, 71.33, 68.79, 69.15, 66.42, 58.22, 69.87, 68.11, 64.27, 61.66, 86.50]

# Сортируем по убыванию прогноза
sorted_data = sorted(zip(forecast, compositions), reverse=True)
forecast_sorted, comp_sorted = zip(*sorted_data)

plt.figure(figsize=(12, 8))
bars = plt.bar(comp_sorted, forecast_sorted, color='#3498db', edgecolor='black', linewidth=1.2)

plt.ylabel('Прогнозируемый выход коллагена, %', fontsize=16)
plt.title('Рисунок 3.3. Топ-12 составов DES по предсказанию MLP-модели\n(R² = 0.987, MAE = 1.78 %)', fontsize=18, pad=20)
plt.ylim(0, 100)
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Подписи над столбцами
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1.5,
             f'{height:.1f}%', ha='center', va='bottom', fontsize=13, fontweight='bold')

plt.xticks(rotation=15, ha='right', fontsize=12)
plt.tight_layout()
plt.savefig("/project/results/Рисунок_3.3_Топ12_только_прогноз_MLP.png", dpi=400, bbox_inches='tight')
plt.close()

print("ГОТОВО! Чистый прогноз MLP — рисунок 3.3 создан")
