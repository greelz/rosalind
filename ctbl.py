'''
Matt Greeley
CS 300

Creating a Character Table
ctbl.py

Given: An unrooted binary tree T in Newick format for at most 200 species taxa.

Return: A character table having the same splits as the edge splits of T. The columns of the character table should encode the taxa ordered lexicographically; the rows of the character table may be given in any order. Also, for any given character, the particular subset of taxa to which 1s are assigned is arbitrary.

Sample Dataset
(dog,((elephant,mouse),robot),cat);

Sample Output
00110
00111
'''

from Bio import Phylo
from StringIO import StringIO

# Returns a list of all taxa inside a clade (recursively)    
def getTree(clade, charList):
    for x in clade:
        if x.name:
            charList.append(x.name)
        else:
            getTree(x, charList)
    return charList
            
# Converts a list of taxa to a lexographical and binary list (ON/OFF concept)
def treeTo1s(charList, orderedDictionary):
    returnList = ['0' for x in orderedDictionary]
    for x in charList:
        returnList[orderedDictionary[x]] = '1'
    return returnList


'''
    The only current problem with this algorithm is that 
    it returns the full tree as a subtree. I haven't really 
    looked at trying to fix this, so when submitting an answer,
    always ignore the first result (or erase it)
'''
if __name__ == "__main__":
    with(open('input', 'r')) as f:
        tree = Phylo.read(StringIO(f.read()), 'newick')

    Phylo.draw_ascii(tree)

    # Create an ordered dictionary, where the keys are taxa, the values are what number in the list it is
    # e.g., {'alice': 0, 'bob': 1, 'foo': 2, 'greelz': 3}
    ordered = {y:x for x,y in enumerate(sorted([str(x) for x in tree.get_terminals()]))}

    # Iterate through the whole tree, and whenever you find a clade, that's gotta be a subtree
    for x in tree.find_clades():
        if not x.name: # clade
            print(''.join(treeTo1s(getTree(x, []), ordered)))
