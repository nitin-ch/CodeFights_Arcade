def findlargest(s):
    maxm = len(s[0])
    for i in range(len(s)):
        if len(s[i]) > maxm:
            maxm = len(s[i])
    return maxm


def allLongestStrings(inputArray):
    mx = findlargest(inputArray)
    longStrings = []
    for i in range(len(inputArray)):
        if len(inputArray[i]) == mx:
            longStrings.append(inputArray[i])
    return longStrings


a = ["aba", "aa", "ad", "vcd", "aba"]
print allLongestStrings(a)
