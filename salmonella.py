
import os

#good to test steps of code by adding print statments after each step (even if
#you're returning an explative rather than a variable)


def fasta_to_string():
    '''Get the file as a single string with no blank space. This would fail if
    there is more than one line of description. Should add a check to look for
    '>' to make sure only sequence is gathered in string.'''

    with open('data/salmonella_spi1_region.fna', 'r') as f:

        #initialize an empty string
        seq = ''

        #Convert each line into a string while concatinating them
        counter = 0
        for line in f:
            if counter != 0:
                seq += line.rstrip()
            #counter += 1 (this method is slower than method used below)
            else:
                counter = 1
        return seq


def gc_content(seq):
    '''function to get the g-c content'''

    gc_content = (seq.count('Gg') + seq.count('Cc'))/ len(seq)

    return gc_content


def gc_blocks(seq, block_size):
    '''This function divides a sequence into blocks and computes
    the GC content for each block, returning a tuple.'''

    #initialize an empty list
    myblocks = []

    #Measure the length of the sequence
    lenth = len(seq)

    #Generate the block. '// is floor division.'
    for i in range(0, lenth//block_size):

        blocks = seq[i*block_size: (i+1)*block_size]
        myblocks.append(gc_content(blocks))

    return tuple(myblocks)


#def gc_map(seq, block_size, gc_thresh):
#"""Find the blocks that are above the g-c threshold you provide"""

    #initialize an empty list
    #high_gc = []

    #for blocks in gc_blocks(seq, block_size):
        #if my


#def new_fasta(mapped_seq)
#"""Write the GC-mapped sequence (with upper and lower characters) to a new
#FASTA file. Use the same description line (which began with a > in the original
#FASTA file) and have line breaks every 60 characters in the sequence."""
#return .fasta
