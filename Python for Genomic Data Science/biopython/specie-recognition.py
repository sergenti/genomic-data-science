# Problem.
# Find out from what species an unknown DNA sequence came from.

from Bio.Blast import NCBIWWW, NCBIXML

fasta_string = open("myseq.fa").read()

#                              program, database, file
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
blast_record = NCBIXML.read(result_handle)

# Parsed BLAST output

print('we found  %s matches' % len(blast_record.alignments))

E_VALUE_THRESH = 0.01

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)
