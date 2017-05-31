def arrayChange(inputArray):
    count = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i + 1] < inputArray[i]:
            diff = inputArray[i] - inputArray[i + 1] + 1
            count += diff
            inputArray[i + 1] += diff
        elif inputArray[i + 1] == inputArray[i]:
            count += 1
            inputArray[i + 1] += 1
    return count
