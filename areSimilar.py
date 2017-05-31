def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def areSimilar(a, b):
    if a == b:
        return True

    for i in range(len(a)):
        for j in range(1, len(b)):
            b[i], b[j] = swap(b[i], b[j])
            # print b
            if a == b:
                return True
            b[i], b[j] = swap(b[i], b[j])
    return False


a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]

print areSimilar(a, b)
