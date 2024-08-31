'''
Frequency Game (GFG)

Given an array A of size N. The elements of the array consist of positive integers. You have to find the largest element with minimum frequency.

Example 1:

Input: 
5
2 2 5 50 1
Output:
50
Explanation :
All elements are having frequency 1 except 2.
50 is the maximum element with minimum frequency.
'''

from collections import Counter
import math

def LargButMinFreq(arr,n):
    dict1=Counter(arr)
    
    max_freq=math.inf
    maximum=-math.inf
    
    for i in dict1:
        if dict1[i]<max_freq:
            maximum=i
            max_freq=dict1[i]
        elif dict1[i]==max_freq:
            if i>maximum:
                maximum=i

    return maximum
