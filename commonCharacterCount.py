def commonCharacterCount(s1, s2):
    itr = min(len(s1), len(s2))
    count = 0

    if len(s1) == itr:
        # print "s1 is shorter"
        for i in range(itr):
            if s1[i] in s2:
                count += 1
                s2 = s2.replace(s1[i], "", 1)
    if len(s2) == itr:
        # print "s2 is shorter"
        for i in range(itr):
            if s2[i] in s1:
                count += 1
                s1 = s1.replace(s2[i], "", 1)
    return count


s1 = 'zzzz'
s2 = 'zzzzzzz'
print commonCharacterCount(s1, s2)
