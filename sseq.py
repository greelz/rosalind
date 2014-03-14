'''
Matt Greeley
CS 300

Problem 21: Finding a Spliced Motif

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
'''

import reader
# Read the file 
dic = reader.fastaToDic('input')

# Collect the two strands by finding the longest/shortest strands
mainStrand = max([v for v in dic.values()], key = lambda x:len(x))
subStrand = min([v for v in dic.values()], key = lambda x:len(x))

# Store the main and substrands, and create counters for both iterators
subIndex, mainIndex, indices = 0, 0, []
for letter in mainStrand:
    # If the letter in mainStrand == letter in substrand, add the index of the main strand to a list, and iterate subIndex. If subIndex == len(subStrand), we've progressed through the substrand and are complete
    if letter == subStrand[subIndex]:
        indices.append(str(mainIndex + 1))
        subIndex += 1
        if subIndex == len(subStrand):
            break
    mainIndex += 1
# Print the answer
print(' '.join(indices))
