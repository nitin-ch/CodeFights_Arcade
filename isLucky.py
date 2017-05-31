def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def isLucky(n):
    length = len(str(n))
    divider = 10**(length / 2)
    firstHalf = n / divider
    secondHalf = n % divider
    if sum_digits(firstHalf) == sum_digits(secondHalf):
        return True
    else:
        return False
