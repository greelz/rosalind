'''
Matt Greeley
CS 300

Problem 9
'''
'''
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''

s = raw_input()
# Create a dictionary to switch letters to their complements
switcher = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
# Print the new, reversed string after list comprehension join
print(''.join([switcher[x] for x in s])[::-1])
