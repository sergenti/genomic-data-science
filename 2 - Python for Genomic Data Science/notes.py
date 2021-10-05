dna = "agggcttcgatcgatcgatcgactcgatagctc"

# =========================================================

# length of string
length = len(dna)

# =========================================================

# indexing
base = dna[2]

# =========================================================

# substring (start included, end excluded)
sub = dna[1:3]

# =========================================================

# basic string operations

'atg' + 'gtacgtccgt'  # 'atggtacgtccgt'
'atg'*3  # 'atgatgatg'
'atg' in 'atggccggcgta'  # True
'n' in 'atgtgggg'  # False

# =========================================================

# counting bases & substrings
dna.count('c')
dna.count('actc')

# =========================================================

# finding first occurance
dna.find('actc')

# finding last occurance
dna.rfind('actc')

# searching substring starting from index i
dna.find('actc', i)

# =========================================================

# switching case
dna.upper()
dna.lower()

# checking case
dna.isLower()
dna.isUpper()

# =========================================================

# replacing
dna.replace('a', 'A')

# =========================================================

# GC content

dna = 'acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag'
no_c = dna.count('c')
no_g = dna.count('g')
dna_length = len(dna)
gc_percent = (no_c + no_g) * 100.0 / dna_length
print(gc_percent)

# =========================================================

# copying list
newalphabet = alphabet[:]

# clearning the list
gene_expression[:] = []

# =========================================================

# using list as stack
stack.append()
stack.pop()

# =========================================================

# sorting a list
# ( the .sort method modifies the list )

mylist.sort()
sorted(mylist)

# =========================================================

# set operations

A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

print("Union :", A | B)
# Union : {0, 1, 2, 3, 4, 5, 6, 8}

print("Intersection :", A & B)
# Intersection : {2, 4}

print("Difference :", A - B)
# Difference : {0, 8, 6}

# =========================================================

# adding & updating keys
dictionary[key] = val

# deleting
del dictionary[key]

# adding multiple keys
dictionary.update({'key1': value1, 'key2': value2, 'key3': value3})

# listing
list(dictionary.keys())
list(dictionary.values())


# =========================================================

# before accessing a key, always check it exist
if key in dictionary:
    pass

# =========================================================

# undefined bases

if 'n' in dna:
    nbases = dna.count('n')
    print("dna sequence has %d undefined bases " % nbases)

# boolen ( in / not in / is / is not )


alphabet = ['a', 'c', 'g', 't']
newalphabet = alphabet[:]
alphabet == newalphabet  # True
alphabet is newalphabet  # False

# =========================================================

# all prime numbers before number N

N = 10
for y in range(2, N):
    for x in range(2, y):
        if y % x == 0:
            print(y, 'equals', x, '*', y//x)
            break
    else:
        # loop fell through without finding a factor
        print(y, 'is a prime number')

# =========================================================

# swapping


def swap2(x, y):
    return(y, x)


def swap3(x, y):
    z = x
    x = y
    y = z
    return(x, y)


def swap4(x, y):
    x, y = y, x
    return(x, y)
