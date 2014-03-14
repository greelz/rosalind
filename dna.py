dna = raw_input()
dic2 = {'A':0, 'C':0, 'G':0, 'T':0}
for symbol in dna:
    dic2[symbol] += 1

print(dic2['A'])
print(dic2['C'])
print(dic2['G'])
print(dic2['T'])
