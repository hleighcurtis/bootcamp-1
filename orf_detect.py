def longest_orf(seq):
"""This takes a DNA sequence as input and finds the longest open reading frame
(ORF) in the sequence (we will not consider reverse complements). A sequence
fragment constitutes an ORF if the following are true.
1)It begins with ATG.
2)It ends with any of TGA, TAG, or TAA.
3)The total number of bases is a multiple of 3."""

 # Initialize list of base pairs
    bps = []
    final = []

    # Scan through string
    for i, x in enumerate(seq):
        triplet = [i + i + 3]
        if triplet == 'ATG':
            bps.append(i)
        elif x == ('TAA', 'TAG', 'TGA'):
            if len(bps) > 0:
                final.append((bps.pop(), i))
                print(final)
            else:
                print('Error in input structure.')
                return False

    # Return the result as a tuple
    return tuple(sorted(final))
