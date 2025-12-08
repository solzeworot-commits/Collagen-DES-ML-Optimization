from Bio import SeqIO
import subprocess
import pandas as pd

subprocess.run(["pepstats", "-sequence", "/project/data/collagen_bioactive_120.fasta",
                "-outfile", "/project/results/peptides_pI_EMBOSS.txt", "-auto"])

# Парсим EMBOSS
data = []
with open("/project/results/peptides_pI_EMBOSS.txt") as f:
    for line in f:
        if line.startswith("PEPSTATS of "):
            name = line.split(" of ")[1].strip()
        if "Isoelectric Point" in line:
            pI = float(line.split("=")[1].strip())
            data.append({"Peptide": name, "pI_EMBOSS": round(pI, 3)})
pd.DataFrame(data).to_excel("/project/results/Приложение_2_pI_EMBOSS.xlsx", index=False)
print("Приложение 2 готово (EMBOSS 6.6.0)")
