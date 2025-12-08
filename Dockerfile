# Dockerfile для диссертации: RDKit + EMBOSS (IPC2 добавим вручную, декабрь 2025)
FROM continuumio/miniconda3:latest

LABEL maintainer="Zaynab Odilova <z.odilova@stgau.ru>"
LABEL description="Воспроизводимая среда для дескрипторов коллагена и pI (спец. 4.3.5)"

# 1. Настраиваем каналы conda
RUN conda config --add channels defaults && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge && \
    conda config --set channel_priority strict

# 2. Создаём окружение с Python 3.11 и всеми пакетами
RUN conda create -n collagen python=3.11 -y && \
    conda install -n collagen -y \
        rdkit=2024.09.5 \
        pandas \
        openpyxl \
        biopython=1.84 \
        molvs \
        emboss=6.6.0 \
    && conda clean --all

# 3. Рабочая папка проекта
WORKDIR /project
COPY . /project

# 4. Активация окружения при запуске
SHELL ["conda", "run", "-n", "collagen", "/bin/bash", "-c"]

CMD ["/bin/bash"]