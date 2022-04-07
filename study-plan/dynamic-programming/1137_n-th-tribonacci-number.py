# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        fib = [0, 1, 1]
        for i in range(3, n+1):
            fib[i%3] = fib[i%3] + fib[(i+1)%3] + fib[(i+2)%3]
        return fib[n%3]