def palindromeRearranging(inputString):
    uniques = list(set(inputString))
    count_char = [i for i in range(len(uniques))]
    # print count_char
    a = 0
    for u in uniques:
        count_char[a] = inputString.count(u)
        a = a + 1
    n_odd = 0
    n_even = 0
    for c in count_char:
        if c % 2 == 0:
            n_even += 1
        else:
            n_odd += 1
    if n_odd == 1 or n_odd == 0:
        return True
    return False


print palindromeRearranging('aabbcc')
