#Question: Given a positive integer n. Your task is to generate a string list of all n-bit binary numbers where, for any prefix of the number, there are more or an equal number of 1's than 0's. The numbers should be sorted in decreasing order of magnitude.
'''Input:  
n = 2
Output: 
"11, 10"
Explanation: Valid numbers are those where each prefix has more 1s than 0s:
11: all its prefixes (1 and 11) have more 1s than 0s.
10: all its prefixes (1 and 10) have more 1s than 0s.
So, the output is "11, 10".'''

'''Input:  
n = 3
Output: 
"111, 110, 101"
Explanation: Valid numbers are those where each prefix has more 1s than 0s.
111: all its prefixes (1, 11, and 111) have more 1s than 0s.
110: all its prefixes (1, 11, and 110) have more 1s than 0s.
101: all its prefixes (1, 10, and 101) have more 1s than 0s.
So, the output is "111, 110, 101".'''

class Solution:
    def NBitBinaryUtil(self, number, extraOnes, remainingPlaces, ans):
        if remainingPlaces == 0:
            ans.append(number)
            return
        
        self.NBitBinaryUtil(number + "1", extraOnes + 1, remainingPlaces - 1, ans)
        
        if extraOnes > 0:
            self.NBitBinaryUtil(number + "0", extraOnes - 1, remainingPlaces - 1, ans)
    
    def NBitBinary(self, n):
        ans = []
        self.NBitBinaryUtil("", 0, n, ans)
        return ans

