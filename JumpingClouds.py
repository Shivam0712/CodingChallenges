#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # return 0 if edge cases are present
    if (len(c) == 0) or (type(c) a!= list):
        return 0
    # initiate variable for jump and position
    jump = 0
    pos = 0

    # The while loop runs only till position is equal to third last spot
    # Reason: after third last spot irrespective of anything the final
    # spot can be reached in 1 jump 
    while pos < len(c)-3: 

        # check if it is possible to jump 2 step ahead of current position 
        if c[pos+2] == 0:
            # update position with 2 steps
            pos = pos + 2
            # increment jump counter by 1
            jump = jump + 1

        # check if it is possible to jump 1 step ahead of current position
        elif c[pos+1] == 0:
            # update position with 1 steps
            pos = pos + 1
            # increment jump counter by 1
            jump = jump + 1

    # add 1 to final jump count(the final jump from third last to final spot)        
    return jump+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
