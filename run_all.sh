#!/bin/bash
echo "Запуск всех расчётов диссертации..."
conda run -n collagen python scripts/1_des_descriptors.py
conda run -n collagen python scripts/2_calculate_pI.py
conda run -n collagen python scripts/3_peptide_descriptors.py
conda run -n collagen python scripts/4_final_with_yield.py
conda run -n collagen python scripts/5_shap_analysis.py
conda run -n collagen python scripts/6_predictions_vs_experiment.py
conda run -n collagen python scripts/visualize_mlp_architecture.py
echo "ВСЁ ГОТОВО! Результаты в results/"
