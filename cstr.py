'''
Matt Greeley
CS 300

cstr.py

Creating a Character Table from Genetic Strings

Given: A collection of at most 100 characterizable DNA strings, each of length at most 300 bp.

Return: A character table for which each nontrivial character encodes the symbol choice at a single position of the strings. (Note: the choice of assigning '1' and '0' to the two states of each SNP in the strings is arbitrary.)
'''

# Get the data
with(open('input', 'r')) as f:
    charList = [str(x[:-1]) for x in f.readlines()]


# Iterate through a specific dna
for i in xrange(len(charList[0])):
    # Create a binary list, with 1s meaning they are equal, 0s otherwise
    temp = [1 if dna[i] == charList[0][i] else 0 for dna in charList]
    # If the sum > 1 and < len(charList) - 1, then it's non-trivial (we care about it),
    # Print it. 
    if sum(temp) > 1 and sum(temp) < len(charList) - 1:
        print(''.join(map(str, temp)))
