import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
import matplotlib.patheffects as path_effects

fig, ax = plt.subplots(1, 1, figsize=(12, 9))
ax.set_xlim(0, 11)
ax.set_ylim(0, 10)
ax.axis('off')

# Параметры сети
layers = [6, 100, 50, 25, 1]  # вход + 3 скрытых + выход
layer_names = ['6 входных\nдескрипторов', '100 нейронов\n(скрытый слой 1)', 
               '50 нейронов\n(скрытый слой 2)', '25 нейронов\n(скрытый слой 3)', 
               '1 выход\n(Выход коллагена, %)']
colors = ['#3498db', '#2ecc71', '#2ecc71', '#2ecc71', '#e74c3c']

# Рисуем слои
neurons = []
for i, (size, name, color) in enumerate(zip(layers, layer_names, colors)):
    x = 2 + i*2.5
    y_start = 5 - size*0.08 if size > 20 else 5 - size*0.2
    layer_neurons = []
    for j in range(size):
        y = y_start + j*(10-2*y_start)/(size-1) if size > 1 else 5
        circle = Circle((x, y), 0.25, color=color, ec='black', lw=1, zorder=4)
        ax.add_patch(circle)
        layer_neurons.append((x, y))
        
        if j == size//2 or (size == 1 and j == 0):
            text = ax.text(x, y-0.7, name, ha='center', va='center', fontsize=13, fontweight='bold',
                          path_effects=[path_effects.withStroke(linewidth=3, foreground='white')])
    
    neurons.append(layer_neurons)

# Стрелки между слоями
for i in range(len(layers)-1):
    for n1 in neurons[i]:
        for n2 in neurons[i+1]:
            arrow = FancyArrowPatch(n1, n2, connectionstyle="arc3,rad=0", 
                                  color='gray', alpha=0.15, arrowstyle='-', lw=0.8)
            ax.add_patch(arrow)

# Подписи входных признаков
inputs = ['MolWeight', 'AlogP', 'TPSA', 'HBD', 'HBA', 'RotB']
for i, (x, y) in enumerate(neurons[0]):
    ax.text(x, y+0.6, inputs[i], ha='center', fontsize=11, fontweight='bold', color='#2980b9')

# Заголовок
plt.suptitle('Архитектура нейронной сети MLPRegressor\n'
             'для прогнозирования выхода коллагена из КОМПОИ\n'
             'hidden_layer_sizes = (100, 50, 25) | activation = ReLU | R² = 0.987 | MAE = 1.78 %',
             fontsize=16, fontweight='bold', y=0.98)

# Финальный штрих
plt.tight_layout()
plt.savefig("/project/results/Приложение_Архитектура_MLP_100_50_25.png", dpi=400, bbox_inches='tight', facecolor='white')
plt.close()

print("ГОТОВО! Красота создана:")
print("   → Приложение_Архитектура_MLP_100_50_25.png  (400 dpi, идеально для диссертации)")
