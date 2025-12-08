from Bio import SeqIO
import subprocess
import pandas as pd
import re

# Запускаем EMBOSS pepstats
subprocess.run([
    "pepstats",
    "-sequence", "/project/data/collagen_120.fasta",
    "-outfile", "/project/results/emboss_output.txt",
    "-auto"
], check=True)

# Парсим результат
data = []
current_id = ""
with open("/project/results/emboss_output.txt") as f:
    for line in f:
        if line.startswith("PEPSTATS of "):
            current_id = line.split(" of ")[1].strip().split()[0]
        if "Isoelectric Point" in line:
            pi = float(re.search(r"Isoelectric Point\s*=\s*([0-9.]+)", line).group(1))
            data.append({"Peptide": current_id, "pI (EMBOSS 6.6.0)": round(pi, 3)})

pd.DataFrame(data).to_excel("/project/results/Приложение_2_pI_пептидов.xlsx", index=False)
print("Приложение 2 готово (EMBOSS 6.6.0)")
