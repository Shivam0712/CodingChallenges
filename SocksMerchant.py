#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # check for edge cases and return 0 if present
    if (n==0) or type(n)!=int:
        return 0
    
    # define an empty dictionary
    socks = {}
    # define variable for counting pairs
    pairs = 0

    # run the loop on each element of ar
    for i in ar:

        # check if the element is already present in the dictionary
        if i in socks.keys():

            # check if the element already has a value 1
            if socks[i] == 1:

                # set the value to 0
                socks[i] = 0

                # add 1 to counter
                pairs = pairs + 1
            
            # if the element does not have a value set it as 1
            else:
                socks[i] = 1    
        
        # if the element is not present in dictionary set it as 1
        else:
            socks[i] = 1
    
    # return pairs
    return(pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
