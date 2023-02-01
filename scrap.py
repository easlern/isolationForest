def getDensity(l):
    l.sort()
    start = l[0]
    end = l[-1]
    w = end - start
    return len(l)*1.0 / w

def getPartition(l):
    for c in range(2, len(l)-1):
        a = l[:c]
        b = l[c:]
        print('** ' + str(c))
        print(str(getDensity(a)))
        print(str(getDensity(b)))