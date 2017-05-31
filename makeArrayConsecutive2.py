def makeArrayConsecutive2(statues):
    minS = min(statues)
    maxS = max(statues)

    return (maxS - minS + 1) - len(statues)
