'''
Matt Greeley
CS 300

Problem 20: RNA Splicing


Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
'''

import reader # Methods for Bioinformatics

# Get a dictionary that changes RNA to proteins
switcher = reader.getAminoSwitcher()
strands = reader.fastaToDic('input')

# Find the important strand (going to be the longest, use lambda len)
importantStrand = max([v for v in strands.values()], key=lambda x:len(x))

# Iterate through the rest of the strands, replacing the important strand's text with nothing if their is a substring
for key in strands:
    if strands[key] != importantStrand:
        importantStrand = importantStrand.replace(strands[key], '')

# Then, replace all the T's with U's, and go from RNA to protein
importantStrand, j = importantStrand.replace('T', 'U'), ''
for i in xrange(0, len(importantStrand), 3):
    j += switcher[importantStrand[i:i + 3]]

# Don't print out 'Stop' at the end
print j[:-4]
