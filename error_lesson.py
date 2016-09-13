
import bioinfo_dicts

def one_to_three(seq):
    seq = seq.upper()

    #Build conversion
    aa_list = []
    for amino_acid in seq:
        if amino_acid in bioinfo_dicts.aa.keys():
            aa_list += [bioinfo_dicts.aa[amino_acid], '-']
        else:
            raise RuntimeError(amino_acid + ' is not a vaild amino acid.')

    return ''.join(aa_list[:-1])


try:
    #try to import this
    import gc_content
    #if it works, save this variable as True
    have_gc = True
except ImportError as e:
    #if it doesin't import, don't stop the program
    #but save this variable as False
    have_gc = False

seq = "ACTATGATCATTGGATCCAGTCAGTC"

#check if it is true or false
if have_gc:
    #use already writen function
    print(gc_content.gc(seq))
else:
    #write it on my own
    print((seq.count('G') + seq.count('C'))/ len(seq))
