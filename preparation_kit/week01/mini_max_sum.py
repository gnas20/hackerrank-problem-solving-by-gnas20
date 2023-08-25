#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    return [sum(sorted(arr)[:4])
    ,sum(sorted(arr)[-4:])]

    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr))
