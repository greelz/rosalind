'''
Matt Greeley
CS 300

tree.py
Completing a Tree

Given: A positive integer n (n<=1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.
'''

with(open('input', 'r')) as f:
    n = int(f.readline())
    tuples = [line.split() for line in f]

print(n - len(tuples) - 1)

