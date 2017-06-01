def arrayMaximalAdjacentDifference(inputArray):
    maxm = 0
    for i in range(len(inputArray) - 1):
        difference = abs(inputArray[i] - inputArray[i + 1])
        if difference > maxm:
            maxm = difference
    return maxm
