'''
Matt Greeley
CS 300

Problem 18: Perfect Matchings and RNA Secondary Structures

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
'''

import reader # fastaToDic
from math import factorial # factorial

# Input the items and iterate through the dic
for k, v in reader.fastaToDic('input').iteritems():
    # Print the factorial of the # of A's, G's
    print(str(factorial(v.count('A')) * factorial(v.count('G'))))
