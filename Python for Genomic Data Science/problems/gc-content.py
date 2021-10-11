# read DNA sequence from user
dna = 'acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag'

# count the number of C’s in DNA sequence
no_c = dna.count('c')

# count the number of G’s in DNA sequence
no_g = dna.count('g')

# determine the length of the DNA sequence
dna_length = len(dna)

# compute the GC%
gc_percent = (no_c+no_g)*100.0/dna_length

# print GC%
print(gc_percent)


def gc(dna):
    "this function computes the GC percentage of a dna sequence"
    nbases = dna.count('n')+dna.count('N')
    gcpercent = float(dna.count('c')+dna.count('C') +
                      dna.count('g') + dna.count('G')
                      ) * 100.0 / (len(dna)-nbases)
    return gcpercent
