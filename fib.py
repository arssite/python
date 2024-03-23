#Question: 
#You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. Since the terms can become very large return the terms modulo 109+7.
class Solution:
    def series(self, n):
        dp = [0,1]
        for i in range(2,n+1):
            x = dp[-1]+dp[-2]
            dp.append(x%(10**9+7))
        return dp
