#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Sort the array in ascending order
    arr.sort()

    # Initialize the minimum unfairness with a large value
    min_unfairness = float('inf')

    # Iterate through the array to find the minimum unfairness for each possible subarray of length k
    for i in range(len(arr) - k + 1):
        current_unfairness = arr[i + k - 1] - arr[i]
        min_unfairness = min(min_unfairness, current_unfairness)

    return min_unfairness

# Sample Input 0
n_0 = 7
k_0 = 3
arr_0 = [10, 100, 300, 200, 1000, 20, 30]

# Sample Output 0
result_0 = maxMin(k_0, arr_0)
print(result_0)

# Sample Input 1
n_1 = 10
k_1 = 4
arr_1 = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]

# Sample Output 1
result_1 = maxMin(k_1, arr_1)
print(result_1)

# Sample Input 2
n_2 = 5
k_2 = 2
arr_2 = [1, 2, 1, 2, 1]

# Sample Output 2
result_2 = maxMin(k_2, arr_2)
print(result_2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()