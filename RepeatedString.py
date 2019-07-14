#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # return 0 for edge cases
    if (s=='') or (type(s)!=str) or (n=='') or (type(n)!=int):
        return 0

    # initiate counter to countA
    countA = 0
    
    # find the truncated length of string to consider in the total n characters
    remainder = n % len(s)
    
    # run loop over length of string s
    for i in range(len(s)):
        # if i is equal to remainder store the current count of 'a' as count in
        # truncated string
        if i==remainder:
            countARem = countA
        # if character s[i] is a increment countA by 1 
        if s[i]=='a':
            countA = countA + 1
    
    # return countA * number of times string 's' completely repeats before n
    # and add countA in the  truncated string 
    return (int(n/len(s))*countA + countARem)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
