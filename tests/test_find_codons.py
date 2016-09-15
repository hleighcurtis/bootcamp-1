# py.test gives the testing functionality
import pytest

import find_codons as fc

# Load test sequence.
seq = ''.join(['ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAACAATGCAGCCCAGAAGA',
'AGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCT',
'GGAGCGGGACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTC',
'GAGCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATTCTGGGCG',
'TGATAGCCGTTGTGCTGCTCATCATCGTTCTGGTGTCGCTTTTCAATTGA'])


def test_find_codon():

    #Where does it find ATG in the nucleotide sequence provided above? Is the result correct?
    assert fc.find_codon('AUG', seq)==-1 # is RNA convereted to DNA?
    assert fc.find_codon('ATG', seq)==0

    # How about AAT?
    assert fc.find_codon('AAT', seq)==54

    # How about the codons TGT and TAA and TAG? What residue do these last two codons encode
    #(for your convenience, standard genetic code)?



    # Does this residue exist in the protein sequence above?
