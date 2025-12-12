import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Данные точно как в твоей диссертации
data = {
    '№': [2, 3, 7, 10],
    'Состав DES': [
        'Холина хлорид – ZnCl₂',
        'Холина хлорид – SnCl₂',
        'Бетаин – лимонная кислота',
        'Холина хлорид – глицерин (контроль)'
    ],
    'Соотношение': ['1:1,7', '1:1,6', '1:1,1', '1:2,0'],
    'Прогноз MLP, %': [84.8, 84.0, 80.8, 77.4],
    'Примечание': [
        'Лучший экспериментально подтверждённый состав',
        'Второй по эффективности',
        'Полностью натуральный NADES (GRAS)',
        'Самый изученный в литературе состав'
    ]
}

df = pd.DataFrame(data)

# Сохраняем таблицу
df.to_excel("/project/results/Таблица_3.5_Выбранные_составы_для_верификации.xlsx", index=False)

# Рисунок 3.3 — бар-чарт (только прогноз MLP)
plt.figure(figsize=(10, 7))
sns.set_style("whitegrid")
bars = plt.barh(df['Состав DES'], df['Прогноз MLP, %'], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
plt.xlabel('Прогнозируемый выход коллагена по MLP-модели, %', fontsize=14)
plt.title('Рисунок 3.3. Прогнозируемый выход коллагена для отобранных составов DES\n(MLP-модель, R² = 0.987)', fontsize=16)
plt.xlim(75, 87)

# Подписи на столбцах
for i, bar in enumerate(bars):
    width = bar.get_width()
    plt.text(width + 0.3, bar.get_y() + bar.get_height()/2, 
             f'{width}%', va='center', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig("/project/results/Рисунок_3.3_Прогноз_выхода_по_MLP.png", dpi=400, bbox_inches='tight')
plt.close()

print("ГОТОВО! Таблица 3.5 и Рисунок 3.3 созданы")
print("Файлы в results/:")
print("   • Таблица_3.5_Выбранные_составы_для_верификации.xlsx")
print("   • Рисунок_3.3_Прогноз_выхода_по_MLP.png")
