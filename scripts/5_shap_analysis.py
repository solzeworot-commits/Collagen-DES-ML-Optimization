import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Загружаем датасет
df = pd.read_csv("/project/results/simulated_DES_collagen_dataset_1240.csv")

# Преобразуем 'Ratio' из '1:2.59' в float (2.59)
df['Ratio_float'] = df['Ratio'].apply(lambda x: float(x.split(':')[1]))

# Выбираем признаки
X_cols = ['Mw_weighted', 'AlogP_weighted', 'TPSA_weighted', 'Temperature_C', 'pH', 'Concentration_%', 'Ratio_float']
X = df[X_cols]
y = df['Yield_collagen_%']

# Обучаем модель
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# SHAP
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# 1. Summary plot
plt.figure(figsize=(10,8))
shap.summary_plot(shap_values, X, show=False)
plt.tight_layout()
plt.savefig("/project/results/Рисунок_5.1_SHAP_summary_plot.png", dpi=400)
plt.close()

# 2. Dependence plot for AlogP
plt.figure(figsize=(10,6))
shap.dependence_plot('AlogP_weighted', shap_values, X, show=False)
plt.tight_layout()
plt.savefig("/project/results/Рисунок_5.2_SHAP_dependence_AlogP.png", dpi=400)
plt.close()

# 3. Dependence plot for TPSA
plt.figure(figsize=(10,6))
shap.dependence_plot('TPSA_weighted', shap_values, X, show=False)
plt.tight_layout()
plt.savefig("/project/results/Рисунок_5.3_SHAP_dependence_TPSA.png", dpi=400)
plt.close()

print("ГОТОВО! 3 SHAP-графика созданы")
