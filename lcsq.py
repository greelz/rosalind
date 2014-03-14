'''
Matt Greeley
CS 300

Problem 24: Finding a Shared Spliced Motif

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
'''

# This function returns the LCS sequence of two strings, s1 & s2. 
# It does so through a method called 'dynamic programming', where a 
# table is built up iteratively, from which values are stored that
# reflect certain aspects of the two strings. To learn more, read about
# LCS at http://en.wikipedia.org/wiki/Longest_common_subsequence_problem
def lcs(s1, s2):
    table = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i][j - 1], table[i - 1][j])
    # Backtrack to get the actual sequence
    return table
                
# LCS(s1, s2) only builds a table. This function backtraces the values 
# of the table to return a string that contains the longest common 
# subsequence. 
def discoverString(table, s1, s2, i, j):
    finalString = ""
    while i != 0 and j != 0:
        if table[i][j] == table[i - 1][j]:
            i -= 1
        elif table[i][j] == table[i][j - 1]:
            j -= 1
        else:
            finalString = s1[i - 1] + finalString
            i -= 1
            j -= 1
    return finalString
        

# Main
import reader

# Get the input and call lcs on both strings
dic = reader.fastaToDic('input')
table = lcs(dic.values()[0], dic.values()[1])
print(discoverString(table, dic.values()[0], dic.values()[1], len(dic.values()[0]), len(dic.values()[1])))
