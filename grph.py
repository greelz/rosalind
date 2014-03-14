'''
Matt Greeley
CS 300

Problem 17: Overlap Graphs


Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
'''
import reader # fastaToDic

dic, n  = reader.fastaToDic('input'), 3

# Iterate through all the items and print the matching suffixes + prefixes
# Since we have an n^2 loop, we will go through every possiblity (of prefix/suffix and suffix/prefix combo)
for x in dic:
    for y in dic:
        if x != y:
            if dic[x][-n:] == dic[y][0:n]:
                print(str(x) + " " + str(y))
