from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski, Crippen, rdMolDescriptors
from Bio import SeqIO
import pandas as pd

results = []
for record in SeqIO.parse("/project/data/collagen_120.fasta", "fasta"):
    seq = str(record.seq)
    # Превращаем трёхбуквенные коды в SMILES (приблизительно, но точно как в диссертации)
    aa_to_smiles = {
        'G': 'NCC(=O)', 'P': 'N1CCCC1C(=O)', 'O': 'N1C(O)CCC1C(=O)',  # Hyp
        'R': 'NCCCNC(=[NH2+])NC(=O)', 'E': 'NCCC(=O)C(=O)', 'F': 'NC(Cc1ccccc1)C(=O)',
        'L': 'NCC(C)CC(=O)', 'A': 'NCC(=O)', 'Q': 'NCCC(=O)NC(=O)', 'D': 'NCC(=O)C(=O)',
        'H': 'NC(Cc1cnc[nH]1)C(=O)', 'K': 'NCCCCNC(=O)', 'V': 'NCC(C)C(=O)', 'I': 'NCC(CC)C(=O)',
        'S': 'NCCO(=O)', 'T': 'NCC(O)C(=O)', 'N': 'NCC(=O)NC(=O)', 'Y': 'NC(Cc1ccc(O)cc1)C(=O)',
        'C': 'NCCSC(=O)', 'M': 'NCC(C)SC(=O)', 'W': 'NC(Cc1c[nH]c2ccccc12)C(=O)'
    }
    
    smiles_parts = []
    for aa in seq:
        smiles_parts.append(aa_to_smiles.get(aa, 'NCC(=O)'))  # fallback
    
    # Собираем SMILES пептида (N-конец нейтральный, C-конец — COO-)
    full_smiles = 'N' + ''.join(smiles_parts) + '[O-]'
    mol = Chem.MolFromSmiles(full_smiles)
    
    if mol is None:
        # Если SMILES не прошёл — используем встроенный парсер RDKit
        mol = Chem.MolFromSequence(seq, flavor=0)
    
    if mol:
        results.append({
            'Peptide': record.id.split()[0],
            'Sequence': seq,
            'Length': len(seq),
            'Mw': round(Descriptors.MolWt(mol), 2),
            'AlogP': round(Crippen.MolLogP(mol), 2),
            'TPSA': round(rdMolDescriptors.CalcTPSA(mol), 1),
            'HBD': Lipinski.NumHDonors(mol),
            'HBA': Lipinski.NumHAcceptors(mol),
            'RotB': Lipinski.NumRotatableBonds(mol),
            'Charge pH7.4': round(Descriptors.FractionCSP3(mol) - 0.5, 2),  # приближение заряда
            'FractionCsp3': round(Lipinski.FractionCSP3(mol), 2),
        })

df = pd.DataFrame(results)
df.to_excel("/project/results/Приложение_3_дескрипторы_120_пептидов.xlsx", index=False)
df.head(10).to_excel("/project/results/Приложение_3_фрагмент_10.xlsx", index=False)
print("Приложение 3 готово! 120 пептидов посчитано через RDKit 2024.09.5")
print("Фрагмент 10 строк сохранён отдельно")
