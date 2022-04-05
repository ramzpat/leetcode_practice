# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        fib = [0, 1, 1]
        for i in range(3, n+1):
            fib[i] = 