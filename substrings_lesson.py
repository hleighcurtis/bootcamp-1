
#This is used to split the string into chunks
def split(s, chunk_size):
    a = zip(*[s[i::chunk_size] for i in range(chunk_size)])
    return [''.join(t) for t in a]


def gen_substrings(my_str1, my_str2):
    """Create all possible substrings"""

    # Initialize sequence length
    if len(my_str1) >= len(my_str2):
        my_str1 = a
        my_str2 = s
    elif len(my_str1) < len(my_str2):
        my_str1 = s
        my_str2 = a

    for base in a:
        if base in split(s, 1):
            print 'y'




my_str1 = 'ATGCATATTTGT'
my_str2 = 'GGACTATCACCG'
