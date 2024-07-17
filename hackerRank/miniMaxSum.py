#!/bin/python3

def miniMaxSum(arr):
    arr = sorted(arr)

    min_sum = arr[0:len(arr)-1]
    max_sum = arr[1:len(arr)]

    return [min_sum, max_sum]

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    
    arr = miniMaxSum(arr)
    print(f"{sum(arr[0])} {sum(arr[1])}")