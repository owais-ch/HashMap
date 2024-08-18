'''
Check if Frequencies can be Equal (GFG)
Given a string s which contains only lower alphabetic characters, check if it is possible to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string.
Return true if it is possible to do else return false.

Note: The driver code print 1 if the value returned is true, otherwise 0.

Example 1:

Input:
s = "xyyz"
Output: 
1 
Explanation: 
Removing one 'y' will make frequency of each character to be 1.
'''

from collections import Counter

class Solution:
    def sameFreq(self, s):
        dict1=Counter(s)
        dict2=Counter(dict1.values())
        
        length=len(dict2)
        
        if len(dict2)>2:
            return 0
        elif len(dict2)==1:
            
            return 1
        elif len(dict2)==2:
            n1,n2=dict2.keys()
            if (n1==1 and dict2[n1]==1) or (n2==1 and dict2[n2]==1):
                return 1
            if abs(n1-n2)==1:
                if n1>n2:
                    if dict2[n1]==1:
                        return 1
                    else:
                        return 0
                else:
                    if dict2[n2]==1:
                        return 1
                    else:
                        return 0
                return 1
        return 0
