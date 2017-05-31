def sortByHeight(a):
    indices = [i for i, x in enumerate(a) if x == -1]
    print indices
    a[:] = [x for x in a if x != -1]
    a.sort()
    for i in indices:
        print i
        a.insert(i, -1)
    return a
