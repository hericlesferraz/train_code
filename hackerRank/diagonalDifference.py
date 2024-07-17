def diagonalDifference(arr):
    diagonal_positive = 0
    diagonal_negative = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                diagonal_positive += arr[i][j]
            if i + j == len(arr) - 1:
                diagonal_negative += arr[i][j]

    return abs(diagonal_positive - diagonal_negative)

# def diagonalDifference(arr):
#     # Write your code here
#     n = len(arr)
    
#     first_d = 0
#     second_d = 0
    
#     for i in range(n):
#         first_d += + arr[i][i]
#         second_d += arr[n - 1 - i][i]
    
#     print(abs(first_d-second_d))
#     return abs(first_d-second_d)

print(diagonalDifference(arr=[[1,2,3], [4, 5, 6], [9, 8, 9]]))