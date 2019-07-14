#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # check
    if (len(c) == 0) or (type(c) != list):
        return 0
    jump = 0
    pos = 0
    while pos < len(c)-3: 
        if c[pos+2] == 0:
                pos = pos + 2
                jump = jump + 1
        elif c[pos+1] == 0:
            pos = pos + 1
            jump = jump + 1
    return jump+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
