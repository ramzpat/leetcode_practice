# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        stair = [0, 1, 2]
        for i in range(3, n+1):
            stair[i%3] = stair[(i+1)%3]+stair[(i+2)%3]
        print(stair)
        return stair[n%3]

s = Solution()
print(s.climbStairs(5))