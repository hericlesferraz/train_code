def flippingMatrix(matrix):
    sum = 0
    n = len(matrix)

    for i in range(n // 2):
        for j in range(n // 2):
            sum += max(matrix[i][j],
                       max(matrix[i][n - 1 - j],
                           max(matrix[n - 1 - i][j], matrix[n - 1 - i][n - 1 - j])))
    print(sum)
    return sum

flippingMatrix(matrix=[[1, 2], [3, 4]])