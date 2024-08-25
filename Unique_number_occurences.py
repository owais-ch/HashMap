'''
Unique Number of Occurences (GFG)

Given an array arr of N integers, the task is to check whether the frequency of the elements in the array is unique or not. Or in other words, there are no two distinct numbers in array with equal frequency.
If all the frequency is unique then return true, else return false.

Example 1:

Input:
N = 5
arr = [1, 1, 2, 5, 5]
Output:
false
Explanation:
The array contains 2 (1’s), 1 (2’s) and 2 (5’s), since the number of frequency of 1 and 5 are the same i.e. 2 times. Therefore, this array does not satisfy the condition.
'''

from collections import Counter

class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        dict1=Counter(arr)
        
        length=len(dict1)
        
        dict2=Counter(dict1.values())
        
        
        if len(dict2)==length:
            return True
            
        return False
