def addBorder(picture):
    new_row = len(picture) + 2
    new_col = len(picture[0]) + 2
    solution = []
    # print new_col, new_row
    for i in range(new_row):
        if i == 0 or i == (new_row - 1):
            solution.append('*' * new_col)
            # print i, solution
        else:
            # print i
            solution.append('*' + picture[i - 1] + '*')
            # print solution
    return solution


mat = ["abc",
       "ded"]
print addBorder(mat)
