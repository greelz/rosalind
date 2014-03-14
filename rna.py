'''
Matt Greeley
CS 300
Problem 8, Rosalind
'''

'''
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''
s = raw_input()
print(''.join([x if x is not 'T' else 'U' for x in s]))
