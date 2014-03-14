'''
Matt Greeley
CS 300

Problem 12

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
'''

# Get the input
s, t = raw_input(), raw_input()
# Print the # of differences [zip() creates a list of tuples]
print(sum(x != y for x, y in zip(s, t)))
