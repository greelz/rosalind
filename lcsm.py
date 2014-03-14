'''
Matt Greeley
CS 300

Problem 19: Finding a Shared Motif

Given: A collection of k (k<=100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
'''


import reader

# Returns a generator for all substrings of a certain string
def substrings(s):
    for k in xrange(1, len(s) + 1):
        for i in xrange(len(s) - k + 1):
            yield s[i:i + k]

dic = reader.fastaToDic('input')

# Get a list of all the substrings of the first fasta entry, then compare these values, from highest to lowest, with the other strings. The first correct entry wins. 

'''
Couple notes: This algorithm is actually pretty quick! I've tested my runtime, and I average about 1.7 seconds to get the answer from rosalind. Is this good or bad? 
'''

original = set(substrings(dic.values()[0]))
second = set(substrings(dic.values()[1]))
intersection = set.intersection(original, second)
# Reverse the sorted list by length, and then check to see if you have a match of all
for x in reversed(sorted(intersection, key=len)):
    if all(x in seq for seq in dic.values()[2:]):
        print(x)
        break
