def alternatingSums(a):
    sum_w = [0, 0]
    for i, w in enumerate(a):
        if i % 2 == 0 or i == 0:
            sum_w[0] += w
        else:
            sum_w[1] += w
    return sum_w
