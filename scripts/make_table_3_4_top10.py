import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np

# Загружаем полные данные
df = pd.read_excel("/project/results/Приложение_4_финальное_с_выходом_150_DES.xlsx")

# Загружаем обученную модель и скалер (они у тебя уже есть)
model = joblib.load("/project/models/mlp_best.pkl")
scaler = joblib.load("/project/models/scaler.pkl")

X = df[['MolWeight','AlogP','TPSA','HBD_total','HBA_total','RotB_total']]
X_scaled = scaler.transform(X)
df['Прогноз_финал_%'] = np.round(model.predict(X_scaled), 2)

# Топ-10
top10 = df.sort_values('Прогноз_финал_%', ascending=False).head(10)[[
    'DES', 'MolWeight', 'AlogP', 'TPSA', 'Прогноз_финал_%'
]].round(2)

top10.index = range(1,11)
top10.to_excel("/project/results/Таблица_3.4_Топ10_предсказанных_составов.xlsx", index_label="№")

print("ГОТОВО! Таблица 3.4 создана")
print(top10.to_string())
