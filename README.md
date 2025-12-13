# Разработка технологии получения коллагеновых пептидов из КОМПОИ с использованием глубоких эвтектических растворителей и машинного обучения

**Кандидатская диссертация** — Одилова Зайнаб Арзикуловна  
Ставропольский государственный аграрный университет, 2026  

Научный руководитель: д.б.н., доцент Шлыков Сергей Николаевич  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)  
[![RDKit 2024.09.5](https://img.shields.io/badge/RDKit-2024.09.5-green.svg)](https://www.rdkit.org/)  
[![scikit-learn 1.5.2](https://img.shields.io/badge/scikit--learn-1.5.2-orange.svg)](https://scikit-learn.org/)

## Содержание репозитория (что здесь есть)

Этот репозиторий содержит **все материалы** диссертационного исследования:
- Исходные данные (fasta с 120 пептидами, csv с дескрипторами)
- Все Python-скрипты (расчёт дескрипторов, генерация датасета, обучение MLP, SHAP-анализ, визуализация)
- Готовые результаты в папке `results/` (таблицы Приложений 1–6, все графики для диссертации)
- Docker-образ для полной воспроизводимости (одна команда — всё запускается)
- Архивная копия с DOI: https://doi.org/10.5281/zenodo.13886547

## Как скачать файлы с репозитория (для любого проверяющего)

1. Перейдите по ссылке: https://github.com/solzeworot-commits/Collagen-DES-ML-Optimization
2. Нажмите зелёную кнопку **"Code"** → **"Download ZIP"**
3. Распакуйте архив — внутри будет вся папка проекта с результатами.

Или клонируйте (если установлен Git):git clone https://github.com/solzeworot-commits/Collagen-DES-ML-Optimization.git

## Как запустить и проверить всё (даже если вы не программист)

**Самый простой способ — Docker (5–10 минут, работает на любом Windows/Mac/Linux)**

1. Установите **Docker Desktop** (бесплатно): https://www.docker.com/products/docker-desktop
2. Откройте командную строку (cmd) в папке проекта
3. Выполните **одну команду**:
docker run --rm -v "%cd%":/project solzeworot/collagen-thesis:2026 bash run_all.sh

Через 5–10 минут в папке `results/` появятся **все таблицы и графики** из диссертации (идентично моим результатам).

**Если Docker не хотите** — просто скачайте ZIP (см. выше) — все готовые файлы уже в `results/`.

## Ключевые научные результаты

- Первое применение металлсодержащих DES для переработки КОМПОИ птицы
- Выход коллагеновых пептидов: **83–85 %** (vs 55–65 % традиционные методы)
- Степень гидролиза (<10 kDa): **91,7–92,7 %** (норматив ≥85 %)
- MLP-модель: **R² = 0.987**, **MAE = 1.78 %**
- Рециклинг DES: **95–96 %**
- Себестоимость: **409–418 руб./кг**
- E-фактор: **0.44**
- Полное соответствие ТР ТС 021/2011 и ГОСТ Р 57498-2017

## Development of Collagen Peptide Extraction Technology from Turkey Bone Residue Using Deep Eutectic Solvents and Machine Learning

**Candidate of Technical Sciences Thesis** — Zaynab A. Odilova  
Stavropol State Agrarian University, 2026  

Supervisor: Prof. Sergey N. Shlykov  

## Repository Contents

This repository contains all materials from the dissertation research:
- Raw data (FASTA with 120 peptides, CSV with descriptors)
- All Python scripts (descriptors calculation, dataset generation, MLP training, SHAP analysis, visualization)
- Ready results in `results/` folder (Appendices 1–6 tables, all dissertation figures)
- Docker image for full reproducibility (one command runs everything)
- Archived version with DOI: https://doi.org/10.5281/zenodo.13886547

## How to Download Files

1. Visit: https://github.com/solzeworot-commits/Collagen-DES-ML-Optimization
2. Click green **"Code"** button → **"Download ZIP"**
3. Unpack — all project files with results will be available.

## How to Run and Verify Results

**Simplest way — Docker (5–10 minutes)**

1. Install Docker Desktop (free): https://www.docker.com/products/docker-desktop
2. Open command prompt in project folder
3. Run one command:
docker run --rm -v "%cd%":/project solzeworot/collagen-thesis:2026 bash run_all.sh

After 5–10 minutes all tables and figures from the dissertation will appear in `results/` folder.

**Without Docker** — just download ZIP (see above) — all ready files are already in `results/`.

Одилова З.А., 2025 / Odilova Z.A., 2025