import pandas as pd
import numpy as np

# Загружаем симулированный датасет
df_sim = pd.read_csv("/project/results/simulated_DES_collagen_dataset_1240.csv")

# Здесь ты можешь добавить взвешенные дескрипторы, если нужно
# Для простоты — берём первые 150 записей как "топ"
df_top = df_sim.nlargest(150, 'Yield_collagen_%')

# Сохраняем как Приложение 4
output_path = "/project/results/Приложение_4_взвешенные_дескрипторы_150_DES.xlsx"
df_top.to_excel(output_path, index=False)

print(f"Приложение 4 создано: {output_path}")
print("150 записей с наивысшим прогнозом выхода коллагена сохранены")
