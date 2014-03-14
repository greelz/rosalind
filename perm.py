from itertools import permutations

with(open('output', 'wb')) as w:
    count = 0
    y = list(permutations(range(1, input() + 1)))
    w.write(str(len(y)) + '\n')
    for x in y:
        w.write(str(x)[1:-1].replace(',', "") + '\n')
