import re
from itertools import takewhile 

# ---------

def proteins(strand):
    codons_in_strand = re.findall('.{3}', strand)
    codons_before_stop = takewhile(lambda c: c not in stop_codons, codons_in_strand)
    return [codon_to_protein[c] for c in codons_before_stop]

# --- human editable information
protein_to_codon = {
        "Methionine": ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
    }
stop_codons = ["UAA", "UAG", "UGA"]

# --- dict data for proteins() function
codon_to_protein = {c: p for p, c_l in protein_to_codon.items() for c in c_l}

# --- quick test
# print(proteins("AUGUUUUCUUAAAUG"))