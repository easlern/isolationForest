def getDensity(l):
    if len(l) < 2:
        return None
    l.sort()
    start = l[0]
    end = l[-1]
    w = end - start
    if w == 0:
        return None
    return len(l)*1.0 / w


def getPartition(l):
    currentDensity = getDensity(l)
    vals = dict()
    for c in range(1, len(l)):
        a = l[:c]
        b = l[c:]
        # print('** ' + str(c))
        d0 = getDensity(a)
        d1 = getDensity(b)
        # print(str(d0))
        # print(str(d1))
        if d0 is None and d1 is None:
            continue
        if d0 is None:
            vals[c] = d1
        elif d1 is None:
            vals[c] = d0
        else:
            vals[c] = d0*d1
    best = None
    for key in vals:
        k = key
        v = vals[k]
        if best is None or v > best[1]:
            best = (k,v)
    if best is None:
        return None
    if best[0] > currentDensity*2:
        return best[0]
    else:
        return None