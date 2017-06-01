# Min. Divisor method
def avoidObstacles(inputArray):
    for n in range(2, 1000):
        # print n
        remainders = [x % n for x in inputArray]
        # print remainders
        if all(v != 0 for v in remainders):
            return n


print avoidObstacles([5, 3, 6, 7, 9])
