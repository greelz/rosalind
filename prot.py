'''
Matt Greeley
CS 300

Problem 14

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
'''

import reader # To get the amino switcher, a little module I made

dic = reader.getAminoSwitcher()
protein = ""
with open('input', 'r') as f:
    for line in f:
        # Read the file, 3 letters at a time
        for i in range(0, len(line) - 1, 3):
        # Add to the protein string the corresponding letter from the dictionary
            protein += dic[line[i:i+3]]

print(protein.replace('Stop', ''))
