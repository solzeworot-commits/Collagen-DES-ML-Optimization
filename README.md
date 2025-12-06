\# Collagen Peptide Extraction from Turkey Bone Residue Using Deep Eutectic Solvents and Machine Learning



\*\*PhD Thesis Repository\*\* – Zaynab A. Odilova  

Stavropol State Agrarian University, 2026  

Supervisor: Prof. Sergey N. Shlykov  



\[!\[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

\[!\[Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)

\[!\[RDKit](https://img.shields.io/badge/RDKit-2024.09.1-green)](https://www.rdkit.org)



\## Key Scientific Results

\- First application of \*\*metal-containing DES\*\* (ChCl–ZnCl₂ 1:1.7, ChCl–SnCl₂ 1:1.6) for poultry bone residue

\- Collagen peptide yield: \*\*83–85%\*\* (vs 55–65% traditional acid/alkali methods)

\- MLP neural network prediction MAE: \*\*1.8%\*\*

\- DES recycling rate: \*\*95–96%\*\*

\- Production cost: \*\*409–418 RUB/kg\*\*

\- E-factor: \*\*0.44\*\* (green chemistry compliant)



\## Full Reproducibility

All results from the dissertation can be reproduced in \*\*one command\*\*:



```bash

conda env create -f environment.yml

conda activate collagen-des

python scripts/reproduce\_all\_results.py

