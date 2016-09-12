""" Convert DNA to RNA """

def rna(seq):
    """Convert DNA sequence to RNA"""

    #Convert to uppercase.
    seq = seq.upper()

    #Exchange T's with U's.
    return seq.replace('T', "U")
