# https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib = [0, 1]
        for i in range(1, n):
            fib[(i+1)%2] = fib[(i+1)%2] + fib[i%2]          
        return fib[n%2]