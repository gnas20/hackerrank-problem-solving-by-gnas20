#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    total_elements = len(arr)
    negative_proportion =[
        sum(1 for num in arr if num > 0)/total_elements, # Proportion of positive 
        sum(1 for num in arr if num < 0)/total_elements, # Proportion of negative
        sum(1 for num in arr if num ==0)/total_elements] # Proportion of zero
    return negative_proportion

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    for each in plusMinus(arr): print("{:.6f}".format(each))
