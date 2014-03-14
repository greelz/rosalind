'''
Matt Greeley
CS 300

Problem 13
'''

'''
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''
# Return the probability of an organism reproducing with itself
def intraorganism(num, percentage):
    return (num - 1) * num * .5 * percentage

# Get the input
k, m, n = [int(x) for x in raw_input().split()]
total = k + m + n

# Calculate the 'guarantee' percentage, the total percentage where we will have an organism possessing at least 1 dominant allele
'''
    YY & YY = 100%
    YY & Yy = 100%
    YY & yy = 100%
    Yy & Yy = 75%
    Yy & yy = 50%
    yy & yy = 0% (never accounted for...)
'''
percentages = intraorganism(k, 1.0) + intraorganism(m, .75) + k * (m + n) + (m * n * .5)

# The answer is the % of orgs with at least 1 dominant allele / total number of possible interactions
print(percentages / intraorganism(total, 1))
