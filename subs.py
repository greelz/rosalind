'''
Matt Greeley
CS 300

Problem 15

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
'''

import re # For re.finditer
# Read the file
with open('input', 'r') as f:
    a = f.read().split()
# s is the original dna string, t is the substring we want
s = a[0]
t = a[1]

# Use regex-look-ahead to find all substrings in s, print out results how the rosalind file wants it
print(' '.join([str(m.start() + 1) for m in re.finditer('(?=' + str(t) + ')', s)]))
