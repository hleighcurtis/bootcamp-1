# py.test gives the testing functionality
import pytest

# We'll use our bioinformatics dictionary from before
import bioinfo_dicts as bd

def n_neg(seq):
    '''Function to compute the number of negative (acidic) residues in a protein sequence.'''

    # Revert to uppercase.
    seq = seq.upper()

    # Check for validity of the sequence.
    for aa in seq:
        if aa not in bd.aa.keys():
            raise RuntimeError(aa + 'is not a valid amino acid')

    # Count E's and D's and return count.
    return seq.count('D') + seq.count('E')
