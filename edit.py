'''
Matt Greeley
CS 300

Problem 22: Edit Distance

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).

Return: The edit distance dE(s,t).
'''

# Calculating the edit distance between two points
def editDistanceTable(s1, s2):
    # Create a table with some initialized values. The table itself holds the memoized values. 
    table = [[j if i == 0 else 0 if j != 0 else i for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
    '''
        This is what the table looks like after initialization
        s1: hello
        s2: mynameismatt
             M  Y  N  A  M  E  I  S  M  A   T   T 
         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
       H [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       E [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       L [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       L [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       O [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    '''

    # Perform dynamic algorithm, learned from the slides. See the picture at this link for more details: 
    # http://en.wikipedia.org/wiki/Edit_distance
    for i in range(0, len(s2)):
        for j in range(0, len(s1)):
            if s2[i] == s1[j]:
                table[i + 1][j + 1] = table[i][j]
            else:
                table[i + 1][j + 1] = min(table[i][j + 1] + 1, table[i + 1][j] + 1, table[i][j] + 1)
    return table

# The actual edit distance is the last element (in the bottom RHS)
def editDistance(s1, s2):
    return editDistanceTable(s1, s2)[len(s2)][len(s1)]


import reader
dic = reader.fastaToDic('input')

print(editDistance(dic.values()[0], dic.values()[1]))
