# without swap
def areSimilar(a, b):
    if a == b:
        return True

    a1 = []
    a2 = []
    for i in range(len(a)):
        if (a[i] != b[i]):
            a1.append(a[i])
            a2.append(b[i])
    if (len(a1) == 2 and (a1 == a2[::-1])):
        return True
    return False
