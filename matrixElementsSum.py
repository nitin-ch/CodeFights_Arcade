def matrixElementsSum(matrix):
    s = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                for a in range(i + 1, len(matrix)):
                    matrix[a][j] = 0
    s = sum(map(sum, matrix))
    return s


m = [[1, 1, 1, 0],
     [0, 5, 0, 1],
     [2, 1, 3, 10]]
print matrixElementsSum(m)
