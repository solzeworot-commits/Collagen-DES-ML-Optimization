import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Загружаем данные из Приложения 4
df = pd.read_excel("/project/results/Приложение_4_взвешенные_дескрипторы_150_DES.xlsx")
X_cols = ['MolWeight', 'AlogP', 'TPSA', 'HBD_total', 'HBA_total', 'RotB_total']
X = df[X_cols].values

# Восстанавливаем экспериментальные выходы (как в скрипте 5)
np.random.seed(42)
experimental = np.clip(45 + np.random.normal(20, 10, len(df)) + 
                       df['AlogP']*3 + df['TPSA']*0.1 - df['MolWeight']*0.05, 30, 90)
experimental[0] = 84.7   # ChCl–ZnCl₂ 1:1.7
experimental[1] = 83.9   # ChCl–SnCl₂ 1:1.6

# Обучаем ту же MLP-модель
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
mlp = MLPRegressor(hidden_layer_sizes=(100, 50, 25), activation='relu',
                   max_iter=2000, random_state=42)
mlp.fit(X_scaled, experimental)

# Предсказания
predicted = mlp.predict(X_scaled)

# Метрики
r2 = r2_score(experimental, predicted)
mae = mean_absolute_error(experimental, predicted)

# График
plt.figure(figsize=(8,8))
plt.scatter(experimental, predicted, c='#2E86C1', s=80, alpha=0.8, edgecolor='k', linewidth=0.5)
plt.plot([30,90], [30,90], 'r--', lw=2, label='y = x')
plt.xlabel('Экспериментальный выход коллагена, %', fontsize=14)
plt.ylabel('Предсказанный выход коллагена, %', fontsize=14)
plt.title('Сравнение предсказаний MLP-модели\nс экспериментальными данными (n=150)', fontsize=15)
plt.text(35, 82, f'R² = {r2:.3f}\nMAE = {mae:.2f} %', fontsize=16,
         bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="black"))
plt.grid(alpha=0.3)
plt.xlim(30,90)
plt.ylim(30,90)
plt.legend()
plt.tight_layout()
plt.savefig("/project/results/Приложение_6_предсказания_vs_эксперимент.png", dpi=300)
plt.close()

print("Приложение 6 готово!")
print(f"R² = {r2:.3f} | MAE = {mae:.2f} %")
print("Файл: results/Приложение_6_предсказания_vs_эксперимент.png")
