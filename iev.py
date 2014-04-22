'''
Matt Greeley

rosalind.info

Calculating Expected Offspring:

Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

e.g., 
Input: 1 0 0 1 0 1

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
e.g., 
Output: 3.5
'''

x = [int(x) for x in raw_input().split()]
print(x[0] * 2 + x[1] * 2 + x[2] * 2 + x[3] * .75 * 2 + x[4])
