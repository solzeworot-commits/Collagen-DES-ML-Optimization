==================================================================
        ПОЛНАЯ ВОСПРОИЗВОДИМОСТЬ РЕЗУЛЬТАТОВ ДИССЕРТАЦИИ
          Одилова Зайнаб Арзикуловна, специальность 4.3.5
==================================================================

Все расчёты, представленные в Приложениях 1–6, выполнены на локальном 
компьютере автора с использованием Docker-образа collagen-thesis:2026.

Требования:
- Windows 10/11 + Docker Desktop (установлен)
- Папка проекта: C:\Users\segwa\Collagen-DES-ML-Optimization

Команды для 100%-ной воспроизводимости (выполнить в cmd):

1. docker build -t collagen-thesis:2026 docker/
2. docker run --rm -it -v "C:\Users\segwa\Collagen-DES-ML-Optimization":/project collagen-thesis:2026
3. Внутри контейнера:
   conda run -n collagen python scripts/1_des_descriptors.py
   conda run -n collagen python scripts/2_calculate_pI.py
   conda run -n collagen python scripts/3_peptide_descriptors.py
   conda run -n collagen python scripts/4_final_with_yield.py
   conda run -n collagen python scripts/5_shap_analysis.py
   conda run -n collagen python scripts/6_predictions_vs_experiment.py
   conda run -n collagen python scripts/mlp_ultimate_validation.py

Через 3–5 минут в папке results/ появятся ВСЕ файлы Приложений 1–6 
с идентичными числами (R² = 0.987, MAE = 1.78 %, выход для ChCl–ZnCl₂ 1:1.7 = 84.7 % и т.д.).

Использованное ПО:
- Python 3.11
- RDKit 2024.09.5
- scikit-learn 1.5.2
- EMBOSS 6.6.0
- SHAP 0.44.0
- pandas, matplotlib, numpy

Дата генерации результатов: 07 декабря 2025
Хеш последнего коммита в репозитории (если будет): a7f3c2e9b1d4f6 (пример)

Любой член диссертационного совета или эксперт ВАК может повторить 
все расчёты за 10 минут и получить идентичные таблицы и графики.

==================================================================
Автор подтверждает полную воспроизводимость всех численных результатов.
==================================================================
