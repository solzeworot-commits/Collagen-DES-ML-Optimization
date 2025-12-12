import numpy as np
import pandas as pd
from datetime import datetime

def generate_des_collagen_dataset(n_samples: int = 1240, seed: int = 42):
    np.random.seed(seed)
    
    # Заглушка дескрипторов (реальные значения берутся из Приложения 1)
    hba_descriptors = pd.read_excel("results/Приложение_1_дескрипторы_DES.xlsx")
    descriptors = hba_descriptors.to_dict('records')
    
    data = []
    for idx in range(n_samples):
        row = np.random.choice(descriptors)
        # Симуляция технологических параметров
        ratio = round(1 + np.random.random() * 2, 2)  # 1:1 до 1:3
        temp = round(30 + np.random.random() * 20, 1)   # 30–50 °C
        ph = round(4 + np.random.random() * 3, 1)      # 4–7
        time_h = int(4 + np.random.random() * 8)       # 4–12 ч
        conc = round(60 + np.random.random() * 30, 1)  # 60–90 %
        
        # Базовый расчёт выхода + шум (как в диссертации)
        base_yield = (70 - abs(row['AlogP']) * 2.5 + row['TPSA'] * 0.08 - row['MolWeight'] * 0.04)
        noise = np.random.normal(0, 3.0)
        yield_collagen = np.clip(base_yield + noise + (temp-40)*0.3 + (ph-5.5)*1.2, 45, 92)
        
        data.append({
            "ID": f"DES_{idx+1:04d}",
            "HBA": row['Component'],
            "HBD": "mixed",
            "Ratio": f"1:{ratio}",
            "Temperature_C": temp,
            "pH": ph,
            "Time_h": time_h,
            "Concentration_%": conc,
            "Mw_weighted": round(row['MolWeight'], 2),
            "AlogP_weighted": round(row['AlogP'], 3),
            "TPSA_weighted": round(row['TPSA'], 1),
            "Yield_collagen_%": round(yield_collagen, 2)
        })
    
    df = pd.DataFrame(data)
    df.attrs["generation_info"] = {
        "date": datetime.now().isoformat(),
        "seed": seed,
        "n_samples": n_samples,
        "author": "Одилова З.А., 2025"
    }
    return df

# Генерация и сохранение
df_simulated = generate_des_collagen_dataset()
df_simulated.to_csv("simulated_DES_collagen_dataset_1240.csv", index=False)
print(f"ГОТОВО! Сгенерировано {len(df_simulated)} записей")
print("Файл: simulated_DES_collagen_dataset_1240.csv")
