import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski, Crippen, rdMolDescriptors

df = pd.read_csv("/project/data/des_components.csv")
results = []
for _, row in df.iterrows():
    mol = Chem.MolFromSmiles(row['SMILES'])
    if mol:
        results.append({
            'Component': row['Component'],
            'MolWeight': round(Descriptors.MolWt(mol), 2),
            'AlogP': round(Crippen.MolLogP(mol), 3),
            'TPSA': round(rdMolDescriptors.CalcTPSA(mol), 2),
            'HBD': Lipinski.NumHDonors(mol),
            'HBA': Lipinski.NumHAcceptors(mol),
            'RotB': Lipinski.NumRotatableBonds(mol),
        })
pd.DataFrame(results).to_excel("/project/results/Приложение_1_дескрипторы_DES.xlsx", index=False)
print("Приложение 1 готово")
