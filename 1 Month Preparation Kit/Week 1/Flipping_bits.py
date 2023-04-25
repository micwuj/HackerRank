#!/bin/python3

import math
import os
import random
import re
import sys


def flippingBits(n):
    
    n = bin(n).replace('0b', '')
    n = list(str(n).zfill(32))
    binary_swap(n)

    n = ''.join(n)
    n = int(n, 2)

    return n

def binary_swap(n):
    for count, i in enumerate(n):
        if n[count] == '0':
            n[count] = '1'
        else:
            n[count] = '0'



n = int(input())

print(flippingBits(n))