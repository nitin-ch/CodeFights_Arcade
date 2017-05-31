def adjacentElementsProduct(inputArray):
    largeProd = 0
    testarray = inputArray
    for n1 in inputArray:
        testarray.pop(testarray.index(n1))
        for n2 in testarray:
            prod = n1 * n2
            if prod > largeProd:
                largeProd = prod
        testarray = inputArray
    return largeProd
