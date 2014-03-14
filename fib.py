'''
Matt Greeley
CS 300

Problem 10

Given: Positive integers n <= 40 and k <= 5.

Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''

# A recursive solution, much like the fibonacci sequence
def Rabbits(n, k):
    if n < 2:
        return n
    else:
    # Return Rabbits * k if they are able to breed
        return Rabbits(n - 1, k) + Rabbits(n - 2, k) * k

# This problem is surprisingly like the fibonacci sequence - with only the *k change
n, k = [int(x) for x in raw_input().split()]
print(Rabbits(n, k))
