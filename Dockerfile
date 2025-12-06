# Официальный Miniforge от conda-forge — идеально для RDKit + ML в 2025–2026
FROM condaforge/miniforge3:latest

# Создаём чистое окружение для проекта
RUN conda create -n collagen-des python=3.11 -y && \
    conda clean --all -y

# Активируем окружение по умолчанию
ENV PATH /opt/conda/envs/collagen-des/bin:$PATH
SHELL ["/bin/bash", "-c"]

# Устанавливаем все пакеты через conda (RDKit, TensorFlow, SHAP и т.д.)
RUN conda install -c conda-forge -n collagen-des \
        pandas \
        numpy \
        scikit-learn \
        tensorflow \
        rdkit=2024.09.1 \
        matplotlib \
        seaborn \
        shap \
        xgboost \
        jupyter \
        openpyxl \
        tqdm \
        biopython \
        pip -y && \
    conda clean --all -y && \
    /opt/conda/envs/collagen-des/bin/pip install molvs

WORKDIR /app
COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["bash"]