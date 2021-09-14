def reverse_string(seq):
    return seq[::-1]


def complement(dna):
    # Return the complementary sequence string
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N',
                      'a': 't', 'c': 'g', 'g': 'c', 't': 'a', 'n': 'n'}

    letters = list(dna)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)

# transtable=dna.maketrans('acgtnACGTN', 'tgcanTGCAN')
# retur ndna.translate(transtable)

def reversecomplement(seq):
    seq = reverse_string(seq)
    seq = complement(seq)
    return seq
