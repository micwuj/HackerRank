#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    left = 0
    right  = 0

    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr)-1-i]

    return abs(left - right)



if __name__ == '__main__':

    n = 3

    arr = [[1, 2, 3],
           [4, 5, 6],
           [9, 8, 9]]

    result = diagonalDifference(arr)
    print(result)