import sys
import reader

dic = reader.fastaToDic('input')

with open('input', 'r') as f:
    dictionary = {'A':[], 'C':[], 'G':[], 'T':[]}
    count, counter = 0, 0
    for line in f:
        if line[0] == '>':
            label = line
        else:
            for dna in line[:-1]:
                if len(dictionary[dna]) <= count:
                    for key in dictionary:
                        dictionary[key].append(0)
                dictionary[dna][count] += 1
                count += 1
            count = 0
        counter += 1

# Dictionary now looks something like this:
'''
A [5, 1, 0, 0, 5, 5, 0, 0]
C [0, 0, 1, 4, 2, 0, 6, 1]
T [1, 5, 0, 0, 0, 1, 1, 6]
G [1, 1, 6, 3, 0, 1, 0, 0]
'''
# Now we need to select the consensus
optimalList = dictionary['A'][:]
numsList = [0 for letter in optimalList]
counter = 0
for key in dictionary:
    for strand in dictionary[key]:
        if strand > numsList[counter]:
            numsList[counter] = strand
            optimalList[counter] = key
        counter += 1
    counter = 0

print "{0}".format("".join(str(i) for i in optimalList))
for key in dictionary:
    sys.stdout.write(str(key) + ': ')
    for num in dictionary[key]:
        sys.stdout.write(str(num) + ' ') 
    print
