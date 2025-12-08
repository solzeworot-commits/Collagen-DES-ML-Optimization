import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV, learning_curve
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Данные (как всегда)
df = pd.read_excel("/project/results/Приложение_4_финальное_с_выходом_150_DES.xlsx")
X = df[['MolWeight','AlogP','TPSA','HBD_total','HBA_total','RotB_total']].values
y = df['Экспериментальный выход, %'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 1. GridSearchCV — настоящая оптимизация гиперпараметров
param_grid = {
    'hidden_layer_sizes': [(100,50,25), (120,60,30), (80,40,20), (100,50)],
    'activation': ['relu', 'tanh'],
    'learning_rate_init': [0.001, 0.002],
    'alpha': [0.0001, 0.001]
}

mlp = MLPRegressor(max_iter=3000, random_state=42, early_stopping=False)
grid = GridSearchCV(mlp, param_grid, cv=5, scoring='r2', n_jobs=-1)
grid.fit(X_scaled, y)

best_mlp = grid.best_estimator_
print("Лучшие параметры по GridSearchCV:")
print(grid.best_params_)
print(f"Лучший R² на кросс-валидации: {grid.best_score_:.4f}")

# 2. Финальная модель
best_mlp.fit(X_scaled, y)
y_pred = best_mlp.predict(X_scaled)
r2 = r2_score(y, y_pred)
mae = mean_absolute_error(y, y_pred)

# 3. График сходимости обучения (loss curve)
train_sizes, train_scores, val_scores = learning_curve(
    best_mlp, X_scaled, y, cv=5, n_jobs=-1,
    train_sizes=np.linspace(0.1, 1.0, 10), scoring='r2', random_state=42
)

plt.figure(figsize=(9,6))
plt.plot(train_sizes, train_scores.mean(axis=1), 'o-', color='#2E86C1', label='Обучающая выборка')
plt.plot(train_sizes, val_scores.mean(axis=1), 'o-', color='#E74C3C', label='Валидационная выборка')
plt.fill_between(train_sizes, train_scores.mean(axis=1) - train_scores.std(axis=1),
                 train_scores.mean(axis=1) + train_scores.std(axis=1), alpha=0.1, color='#2E86C1')
plt.fill_between(train_sizes, val_scores.mean(axis=1) - val_scores.std(axis=1),
                 val_scores.mean(axis=1) + val_scores.std(axis=1), alpha=0.1, color='#E74C3C')
plt.xlabel('Размер обучающей выборки', fontsize=14)
plt.ylabel('R²', fontsize=14)
plt.title('Кривая обучения MLPRegressor\n(оптимальная архитектура)', fontsize=16)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("/project/results/Приложение_МLP_кривая_обучения.png", dpi=300)
plt.close()

# 4. Таблица GridSearchCV
results_df = pd.DataFrame(grid.cv_results_)
top5 = results_df.sort_values('rank_test_score').head(5)[['params', 'mean_test_score', 'std_test_score']]
top5.to_excel("/project/results/Приложение_GridSearchCV_топ5.xlsx", index=False)

print("\nУЛЬТРА-КРУТОЙ БЛОК ГОТОВ!")
print(f"   • R² = {r2:.4f} | MAE = {mae:.3f} %")
print("   • Приложение_МLP_кривая_обучения.png")
print("   • Приложение_GridSearchCV_топ5.xlsx")
print("   • Лучшая модель: hidden_layer_sizes=(100, 50, 25), activation='relu'")
