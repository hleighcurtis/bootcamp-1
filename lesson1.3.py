
def reverse_complement2(seq):
    """Compute reverse complemnt of a nucleic acid sequence."""

    #reversing the sequence
    seq[::-1]
    #could have made everything lower() to aviod the aliases and better allow to give out answers in RNA

    #exchanging the vocbulary
    seq1 = seq.replace('Uu', 'F')
    seq2 = seq1.replace('Tt', 'I')
    seq3 = seq2.replace('Aa', 'V')
    seq4 = seq3.replace('Gg', 'E')
    seq5 = seq4.replace('Cc', 'S')

    #echanging back complementary vocabulary
    seq6 = seq5.replace('F', 'A')
    seq7 = seq6.replace('I', 'A')
    seq8 = seq7.replace('V', 'T')
    seq9 = seq8.replace('E', 'C')
    seq10 = seq9.replace('S', 'G')

    return seq10
