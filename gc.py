'''
Matt Greeley
CS 300

Problem 11

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

import reader # Used to read in a dictionary from file

# Count and return the GC content in a dna strand (0 - 100.0)
def getGCcontent(dna):
    return float(dna.count('G') + dna.count('C')) / len(dna) * 100

# Read the dictionary from a file, named 'file'
dic = reader.fastaToDic('input')

maxGC = 0
for item in dic:
    px = getGCcontent(dic[item])
    # If we have a % value greater than a previous, set it and label it
    if px > maxGC:
        maxLabel = item
        maxGC = px
        
print(maxLabel)
print(maxGC)
