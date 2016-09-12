codon = input('Input your codon, please')

if codon == 'AUG':
    print('This codon is the start codon.')
else:
    if codon == 'UAA'or codon == 'UAG'or codon== 'UAG':
        print('This is a stop codon.')
    else:
        print('This codon in neither a start or stop codon.')
print('This always prints.')


if codon == 'AUG':
    print('This codon is the start codon.')
elif codon == 'UAA'or codon == 'UAG'or codon== 'UAG':
    print('This is a stop codon.')
else:
    print('This codon in neither a start or stop codon.')
print('This always prints.')

codon_list = ['UAA', 'UAG', 'UGA']
if codon == 'AUG':
    print('This codon is the start codon.')
elif codon == codon_list:
    print('This is a stop codon.')
else:
    print('This codon in neither a start or stop codon.')
print('This always prints.')

codon_tuple = ('UAA', 'UAG', 'UGA')
if codon == 'AUG':
    print('This codon is the start codon.')
elif codon == codon_tuple:
    print('This is a stop codon.')
else:
    print('This codon in neither a start or stop codon.')
print('This always prints.')
