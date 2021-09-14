'''



(1)

- How many records are in the file?

A record in a FASTA file is defined as a single-line header, followed by lines of sequence data.
The header line is distinguished from the sequence data by a greater-than (">") symbol in the first column.
The word following the ">" symbol is the identifier of the sequence, and the rest of the line is an optional description of the entry.
There should be no space between the ">" and the first letter of the identifier.



(2)

- What are the lengths of the sequences in the file?
- What is the longest sequence and what is the shortest sequence?
- Is there more than one longest or shortest sequence? What are their identifiers?



(3)

- What is the length of the longest ORF in the file?
- What is the identifier of the sequence containing the longest ORF?
- For a given sequence identifier, what is the longest ORF contained in the sequence represented by that identifier?
- What is the starting position of the longest ORF in the sequence that contains it?

In molecular biology, a reading frame is a way of dividing the DNA sequence of nucleotides into a set of consecutive,
non-overlapping triplets (or codons). Depending on where we start, there are six possible reading frames:
three in the forward (5' to 3') direction and three in the reverse (3' to 5').

For instance, the three possible forward reading frames for the sequence AGGTGACACCGCAAGCCTTATATTAGC are:

AGG TGA CAC CGC AAG CCT TAT ATT AGC
A GGT GAC ACC GCA AGC CTT ATA TTA GC
AG GTG ACA CCG CAA GCC TTA TAT TAG C

These are called reading frames 1, 2, and 3 respectively. An open reading frame (ORF) is the part of a reading frame that has the potential to encode a protein.
It starts with a start codon (ATG), and ends with a stop codon (TAA, TAG or TGA). For instance, ATGAAATAG is an ORF of length 9.

Given an input reading frame on the forward strand (1, 2, or 3) your program should be able to identify all ORFs present in each sequence of the FASTA file,
and answer the previous questions



(4)

A repeat is a substring of a DNA sequence that occurs in multiple copies (more than one) somewhere in the sequence.
Although repeats can occur on both the forward and reverse strands of the DNA sequence, we will only consider repeats on the forward strand here.
Also we will allow repeats to overlap themselves. For example, the sequence ACACA contains two copies of the sequence ACA.

Given a length n, your program should be able to identify all repeats of length n in all sequences in the FASTA file.
Your program should also determine how many times each repeat occurs in the file, and which is the most frequent repeat of a given length.




'''


import sys
filename = sys.argv[1]

# Opening file from given filename

try:
    f = open(filename)
    print("opening file in %s" & filename)
except IOError:
    print("File %s does not exist!!" % filename)

# Processing fasta file

seqs = {}
count = 0

for line in f:

    line = line.rstrip()

    if line.startswith('>'):  # header
        words = line.split()
        name = words[0][1:]
        seqs[name] = ''

    else:  # sequence
        seqs[name] = seqs[name] + line
        count += 1
close(f)

# (1) How many records are in the file?

print("there are %s records of which %s are unique" % count, len(seqs))

# (2) What are the lengths of the sequences in the file?

lengths = []
for ID, sequence in seqs.items():
    lengths.append(len(sequence))

# (2) What is the longest sequence and what is the shortest sequence?

longest_seq = max(lengths)
shortest_seq = min(lengths)

# (2) Is there more than one longest or shortest sequence? What are their identifiers?

longest_seq_ids = []
shortest_seq_ids = []

for ID, sequence in seqs.items():

    if seqs[ID] == longest_seq:
        longest_seq_ids.append(ID)

    if seqs[ID] == shortest_seq:
        shortest_seq_ids.append(ID)

print("longest sequence is %s base pairs, at id: %s" %
      longest_seq, longest_seq_ids)
print("shortest sequence is %s base pairs, at id: %s" %
      shortest_seq, shortest_seq_ids)
