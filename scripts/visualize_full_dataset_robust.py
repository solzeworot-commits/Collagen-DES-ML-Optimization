import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("/project/results/simulated_DES_collagen_dataset_1240.csv")

print("Столбцы в датасете:", df.columns.tolist())

# Попробуем найти нужные столбцы по ключевым словам
temp_col = next((c for c in df.columns if 'temp' in c.lower() or 'temperature' in c.lower()), None)
ph_col = next((c for c in df.columns if 'ph' in c.lower()), None)
yield_col = next((c for c in df.columns if 'yield' in c.lower() or 'выход' in c.lower()), None)
conc_col = next((c for c in df.columns if 'conc' in c.lower() or 'concentration' in c.lower()), None)
ratio_col = next((c for c in df.columns if 'ratio' in c.lower() or 'соотношение' in c.lower()), None)

if not all([temp_col, ph_col, yield_col, conc_col]):
    print("Не все столбцы найдены — проверьте названия")
else:
    # 1. 3D
    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(df[temp_col], df[ph_col], df[yield_col], 
                    c=df[conc_col], cmap='viridis', s=30, alpha=0.7)
    ax.set_xlabel(temp_col)
    ax.set_ylabel(ph_col)
    ax.set_zlabel(yield_col)
    ax.set_title('3D visualization (n=1240)')
    plt.colorbar(sc, label=conc_col)
    plt.tight_layout()
    plt.savefig("/project/results/Visualization_3D.png", dpi=400)
    plt.close()

    # 2. Heatmap
    if ratio_col:
        pivot = df.pivot_table(values=yield_col, index=ratio_col, columns=temp_col, aggfunc='mean')
        plt.figure(figsize=(12,8))
        sns.heatmap(pivot, annot=False, cmap='YlGnBu')
        plt.title('Heatmap: average yield by ratio and temperature')
        plt.xlabel(temp_col)
        plt.ylabel(ratio_col)
        plt.tight_layout()
        plt.savefig("/project/results/Visualization_Heatmap.png", dpi=400)
        plt.close()

    # 3. Pairplot
    sns.pairplot(df[[temp_col, ph_col, conc_col, yield_col]], diag_kind='kde')
    plt.suptitle('Pairplot key parameters (n=1240)', y=1.02)
    plt.tight_layout()
    plt.savefig("/project/results/Visualization_Pairplot.png", dpi=400)
    plt.close()

    # 4. Histogram
    plt.figure(figsize=(10,6))
    plt.hist(df[yield_col], bins=50, color='#27ae60', edgecolor='black')
    plt.axvline(x=85, color='red', linestyle='--', linewidth=3, label='Normative ≥85 %')
    plt.xlabel(yield_col)
    plt.ylabel('Frequency')
    plt.title('Distribution of predicted yield (n=1240)')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("/project/results/Visualization_Histogram.png", dpi=400)
    plt.close()

    print("ГОТОВО! 4 графика созданы")
