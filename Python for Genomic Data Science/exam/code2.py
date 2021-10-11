from Bio import SeqIO
from collections import Counter


# calculate the start position and the length of longest ORF in sequence
def orf(sequence, reading_frame):
    seq = sequence[reading_frame-1:]
    max_len_orf = 0
    max_orf_start = 0

    for i in range(0, len(seq) - 6, 3):
        if seq[i:i + 3] == 'ATG':
            for j in range(i + 3, len(seq) - 3, 3):
                if seq[j:j + 3] in ['TAA', 'TAG', 'TGA']:
                    len_orf = j+3-i
                    if len_orf > max_len_orf:
                        max_len_orf = len_orf
                        max_orf_start = i
                    break

    return max_orf_start, max_len_orf


# identify all repeats of length n in sequence
def repeat_substring(sequence, repeat_num):
    sub_list = []
    for i in range(len(sequence)-repeat_num):
        sub_list.append(sequence[i:(i+repeat_num)])
    return sub_list


def fasta_analysis(input_file, reading_frame, n):

    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')

    record_num = 0
    record_len = {}
    orf_record = {}
    sub_sum = []

    for fasta in fasta_sequences:
        name, sequence, description = fasta.id, str(fasta.seq), str(fasta.description).split()
        record_num += 1
        seq_len = len(sequence)
        record_len[description[0]] = seq_len

        # calculate the start position and the length of longest ORF
        orf_start, orf_len = orf(sequence, reading_frame)
        orf_record[description[0]] = [orf_start, orf_len]

        # identify all repeats of length n
        substring_list = repeat_substring(sequence, n)
        for i in range(len(substring_list)):
            sub_sum.append(substring_list[i])

    record_len_sorted = {k: v for k, v in sorted(record_len.items(), key=lambda item: item[1], reverse=True)}
    orf_record_sorted = {k: v for k, v in sorted( orf_record.items(), key=lambda item: item[1][1], reverse=True)}

    print("Number of records: ", record_num, '\n')
    print("Sorted records length: ", record_len_sorted, '\n')
    print("ORF%s, sorted by length: " % (reading_frame), orf_record_sorted, '\n')
    print("Counter of repeats of length n, most common 5: ", Counter(sub_sum).most_common(5))


if __name__ == '__main__':
    input_file = 'dna2.fasta'


fasta_analysis(input_file, 1, 7)
