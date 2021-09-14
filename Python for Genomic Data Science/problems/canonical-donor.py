# Problem:
# Given a DNA sequence Hind the positions of all canonical donor splice site candidates in the sequence.

dna = input('Enter DNA sequence:')
pos = dna.find('gt', 0)  # position of donor splice site
while pos > -1:
    print("Donor splice site candidate at position % d" % pos)
    pos = dna.find('gt', pos+1)
