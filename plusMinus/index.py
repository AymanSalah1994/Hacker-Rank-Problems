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
    plus = 0
    minus = 0
    zero = 0
    for item in arr:
        if item > 0:
            plus += 1
        elif item == 0:
            zero += 1
        elif item < 0:
            minus += 1
    print(format(round(plus / n , 6 ) , '6f'))
    print(format(round(minus / n , 6 ) , '6f'))
    print(format(round(zero / n, 6), '6f'))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
