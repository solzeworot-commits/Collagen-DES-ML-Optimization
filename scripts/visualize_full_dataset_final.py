import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("/project/results/simulated_DES_collagen_dataset_1240.csv")

# 1. 3D
fig = plt.figure(figsize=(12,9))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(df['Temperature'], df['pH'], df['Yield_collagen_%'], 
                c=df['Concentration_DES_%'], cmap='viridis', s=30, alpha=0.7)
ax.set_xlabel('Temperature, °C')
ax.set_ylabel('pH')
ax.set_zlabel('Yield collagen, %')
ax.set_title('3D visualization of simulated dataset (n=1240)')
plt.colorbar(sc, label='Concentration DES, %')
plt.tight_layout()
plt.savefig("/project/results/Visualization_3D.png", dpi=400)
plt.close()

# 2. Heatmap
pivot = df.pivot_table(values='Yield_collagen_%', index='Molar_ratio', columns='Temperature', aggfunc='mean')
plt.figure(figsize=(12,8))
sns.heatmap(pivot, annot=False, cmap='YlGnBu')
plt.title('Heatmap: average yield by ratio and temperature (n=1240)')
plt.xlabel('Temperature, °C')
plt.ylabel('Molar ratio')
plt.tight_layout()
plt.savefig("/project/results/Visualization_Heatmap.png", dpi=400)
plt.close()

# 3. Pairplot
sns.pairplot(df[['Temperature', 'pH', 'Concentration_DES_%', 'Yield_collagen_%']], diag_kind='kde')
plt.suptitle('Pairplot key parameters (n=1240)', y=1.02)
plt.tight_layout()
plt.savefig("/project/results/Visualization_Pairplot.png", dpi=400)
plt.close()

# 4. Histogram
plt.figure(figsize=(10,6))
plt.hist(df['Yield_collagen_%'], bins=50, color='#27ae60', edgecolor='black')
plt.axvline(x=85, color='red', linestyle='--', linewidth=3, label='Normative ≥85 %')
plt.xlabel('Collagen yield, %')
plt.ylabel('Frequency')
plt.title('Distribution of predicted yield (n=1240)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("/project/results/Visualization_Histogram.png", dpi=400)
plt.close()

print("ГОТОВО! 4 графика созданы в results/")
