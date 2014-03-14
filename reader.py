def fastaToDic(filename):
    with(open(filename, 'r')) as f:
        dic, strandName, strand = {}, "", ""
        for line in f:
            if line[0] == '>':
                if strandName != "":
                    dic[strandName] = strand
                strandName = line[1:-1]
                strand = ""
            else:
                strand += line[:-1]
    dic[strandName] = strand
    return dic


def getAminoSwitcher():
    with(open('rnaCodon', 'r')) as f:
        s = f.read().split()
    dic = dict(s[i:i+2] for i in range(0, len(s), 2))
    return dic

