#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # return 0 if edge cases are present 
    if (n==0) or (type(n)!=int):
        return 0
    
    # initiate counter for valley
    valley = 0
    
    # initiate variable to keep track of altitude
    alt = 0

    # run a loop on all elements in steps
    for i in s:

        # if the step is U increment altitude by 1
        if i == 'U':
            alt = alt +1
        # if the step is D decrease altitude by 1
        if i == 'D':
            alt = alt -1
        # if the altitude is 0 and step is up then add 1 to valley
        if (alt==0) & (i=='U'):
            valley = valley + 1
    
    # return valley
    return valley
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
