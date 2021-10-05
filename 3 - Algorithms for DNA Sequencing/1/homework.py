# Implement a version of the naive exact matching algorithm that is strand-aware.
# That is: instead of looking only for occurrences of P in T, additionally look for occurrences of thereverse complement of P in T.
# If P is ACT, your function should find occurrences of both ACTand its reverse complement AGT in T.
# If P and its reverse complement are identical (e.g. AACGTT), then a given match offset should be reported only once.

# Hint: See this notebook for a few examples you can use to test your naive_with_rc function.

# Next, download and parse the lambda virus genome, at: https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa


def readGenome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def reverseComplement(s):
    """given the strand 5-3 return the strand 3-5"""
    complement = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N"}
    t = ""
    for base in s:
        t = complement[base] + t
    return t


def leftmostOccurrence(pattern, genome):
    firstForward = genome.find(pattern)
    firstReverse = genome.find(reverseComplement(pattern))
    print(min(firstForward, firstReverse))


def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i + j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences


def NaiveRC(pattern, genome):
    matches = naive(pattern, genome)
    if reverseComplement(pattern) != pattern:
        matches.extend(naive(reverseComplement(pattern), genome))
    return matches


def kmerFinder(pattern, genome):
    print(len(NaiveRC(pattern, genome)))


def completeNaiveRC(reads, genome):
    numMatched = 0
    alignments = 0
    for r in reads:
        r = r[:30]
        matches = naive(r, genome)
        if reverseComplement(r) != r:
            matches.extend(naive(reverseComplement(r), genome))
        alignments += 1
        if len(matches) > 0:
            numMatched += 1
    print("%d / %d reads matched the genome exactly!" % (numMatched, alignments))


############################################################################################################

lambda_virus = readGenome("lambda_virus.fa")
# myReads, _ = readFastq("ERR266411_1.first1000.fastq")

############################################################################################################

# How many times does AGGT or its reverse complement (ACCT) occur in the lambda virus genome?
# # E.g. if AGGT occurs 10 times and ACCT occurs 12 times, you should report 22.

kmerFinder("AGGT", lambda_virus)

############################################################################################################

# How many times does TTAA or its reverse complement occur in the lambda virus genome?
# Hint: TTAA and its reverse complement are equal, so remember not to double count.

kmerFinder("TTAA", lambda_virus)

############################################################################################################

# What is the offset of the leftmost occurrence of ACTAAGT or its reverse complement in the Lambda virus genome?
# E.g. if the leftmost occurrence of ACTAAGT is at offset 40 (0-based) and the leftmost occurrence of its reverse
# complement ACTTAGT is at offset 29, then report 29.

leftmostOccurrence("ACTAAGT", lambda_virus)

# or min(NaiveRC("ACTAAGT", lambda_virus))

############################################################################################################

# What is the offset of the leftmost occurrence of AGTCGA or its reverse complement in the Lambda virus genome?

leftmostOccurrence("AGTCGA", lambda_virus)

# or min(NaiveRC("AGTCGA", lambda_virus))

############################################################################################################

# As we will discuss, sometimes we would like to find approximate matches for P in T. That is, we want to find occurrences with one or more differences.
# For Questions 5 and 6, make a new version of the naive function called naive_2m that allows up to 2 mismatches per occurrence.
# Unlike for the previous questions, do not consider the reverse complement here. We're looking for approximate matches for P itself, not its reverse complement.

# For example, ACTTTA occurs twice in ACTTACTTGATAAAGT, once at offset 0 with 2 mismatches, and once at offset 4 with 1 mismatch. So naive_2mm('ACTTTA', 'ACTTACTTGATAAAGT') should return the list [0, 4].

# How many times does TTCAAGCC occur in the Lambda virus genome when allowing up to 2 mismatches?


def KmerFinderWithMismatches(p, t, m):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        count_mismatch = 0
        for j in range(len(p)):
            if t[i + j] != p[j]:
                count_mismatch += 1
        if count_mismatch <= m:
            occurrences.append(i)
    return occurrences


print(len(KmerFinderWithMismatches("TTCAAGCC", lambda_virus, 2)))

############################################################################################################

# What is the offset of the leftmost occurrence of AGGAGGTT in the Lambda virus genome when allowing up to 2 mismatches?

print(min(KmerFinderWithMismatches("AGGAGGTT", lambda_virus, 2)))
