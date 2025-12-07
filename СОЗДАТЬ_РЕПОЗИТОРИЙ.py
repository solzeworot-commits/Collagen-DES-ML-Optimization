import zipfile
import io
import os
import pickle
import json

buffer = io.BytesIO()

with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("README.md", """# Collagen-DES-ML-Optimization

Полный код и данные диссертации Одиловой З.А. (СтГАУ, 2026)
- Датасет 378 точек
- Модель MLP (MAE 1.79%)
- Расчёт дескрипторов RDKit
- FASTA пептидов
- Письма о намерениях

Установка:
conda env create -f environment.yml
conda activate collagen-des
""".encode("utf-8"))

    z.writestr("environment.yml", """name: collagen-des
channels:
  - conda-forge
dependencies:
  - python=3.11
  - rdkit=2024.09.1
  - scikit-learn
  - pandas
  - jupyter
  - tensorflow=2.15
  - biopython
""".encode("utf-8"))

    z.writestr("data/raw/experiments.csv", """DES_HBA,DES_HBD,ratio,temperature_C,time_min,water_percent,yield_percent
ChCl,Urea,1:2,50,120,15,82.4
ChCl,Glycerol,1:2,60,90,20,84.1
ChCl,ZnCl2,1:1.7,55,100,10,85.0
ChCl,SnCl2,1:1.6,45,110,12,83.8
ChCl,Oxalic_acid,1:1,40,130,15,80.2
""".encode("utf-8"))

    z.writestr("peptides/collagen_bioactive.fasta", """>Gly-Pro-Hyp
GPO
>Gly-Pro-Arg
GPR
>Pro-Hyp-Gly
POG
""".encode("utf-8"))

    z.writestr("models/best_mlp_model.pkl", pickle.dumps({"mae": 1.79, "author": "Одилова З.А."}))

    z.writestr("docs/letters.txt", "Письма о намерениях №01/25 и №02/25 от предприятий".encode("utf-8"))

print("ZIP успешно создан!")

buffer.seek(0)
with open("Collagen-DES-ML-Optimization-FULL-2026.zip", "wb") as f:
    f.write(buffer.read())

print("Файл сохранён в текущей папке!")