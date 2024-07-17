
import math
import os
import random
import re
import sys


def plusMinus(arr):
    resuls_zero = 0
    results_positive = 0
    results_negative = 0

    for number in arr:
        if number == 0:
            resuls_zero += 1
        
        elif number > 0:
            results_positive += 1

        elif number < 0:
            results_negative += 1

    return [results_positive, results_negative, resuls_zero]

if __name__=="__main__":
    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))
    arr = [-4, 3, -9, 0, 4, 1]
    result = plusMinus(arr)
    print(f"{result[0]/len(arr):6f}")
    print(f"{result[1]/len(arr):6f}")
    print(f"{result[2]/len(arr):6f}")
