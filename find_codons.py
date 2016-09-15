

def find_codon(codon, seq):
    """Find a specified codon with a given sequence."""

    # Convert RNA to DNA
    seq = seq.replace('U', 'T')



    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 1

    if i == len(seq):
        return -1

    return i
