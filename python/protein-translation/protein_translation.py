import re
from itertools import takewhile 

def proteins(strand):
    codons_in_strand = re.findall('.{3}', strand)
    codons_before_stop = takewhile(lambda c: c not in ["UAA", "UAG", "UGA"], codons_in_strand)
    return [protein for codon in codons_before_stop for protein, codon_list in codon_to_protein.items() if codon in codon_list]

codon_to_protein = {
        "Methionine": ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
    }

print(proteins("AUGUUUUCUUAAAUG"))
