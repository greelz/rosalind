'''
Matt Greeley
CS 300

nkew.py
Newick Format with Edge Weights

Given: A collection of n weighted trees (n<=40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.

Return: A collection of n numbers, for which the kth number represents the distance between xk and yk in Tk.
'''

from StringIO import StringIO
from Bio import Phylo
import sys

with(open('input', 'r')) as f:
    pairs = [line.split('\n') for line in f.read().strip().split('\n\n')]

for pair in pairs:
    sys.stdout.write(str(int(Phylo.read(StringIO(pair[0]), 'newick').distance(pair[1].split(' ')[0], pair[1].split(' ')[1]))) + ' ')

print
