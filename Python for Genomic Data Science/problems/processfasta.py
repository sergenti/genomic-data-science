"""
processfasta.py builds a dictionary with all sequences from a FASTA file.

script can be executed by the following command:
python processfasta.py myfile.fa

"""

import sys
import getopt
filename = sys.argv[1]


def usage(): print("""""

processfasta.py : reads a FASTA file and builds a dictionary with all sequences bigger than a given length

processfasta.py [-h] [-l <length>] <filename>

-h <help>           print this message 

-l <length>         filter all sequences with a length smaller than <length>
                    (default <length>=0)

<filename>          the file has to be in FASTA format

""")


o, a = getopt.getopt(sys.argv[1:], 'l:h')
opts = {}
seqlen = 0


for k, v in o:
    opts[k] = v
    if '-h' in opts.keys():
        usage()
        sys.exit()
    if len(a) < 1:
        usage()
        sys.exit('input fasta file is missing')
    if '-l' in opts.keys():
        if int(opts['l']) < 0:
            print('Length of sequence should be positive!')
            sys.exit(0)
        seqlen = opts['-l']

try:
    f = open(filename)
except IOError:
    print("File %s does not exist!!" % filename)

seqs = {}

for line in f:
    # discard the newline at the end (if any)
    line = line.rstrip()

    # distinguish header from sequence
    if line.startswith('>'):
        words = line.split()
        name = words[0][1:]
        seqs[name] = ''
    else:  # sequence, not header
        seqs[name] = seqs[name] + line

close(f)


# retriving data
for name, seq in seqs.items():
    print(name, seq)
