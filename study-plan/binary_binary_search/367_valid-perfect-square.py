# https://leetcode.com/problems/valid-perfect-square/

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        
        left, right = 1, num-1
        while left <= right:
            mid = (left + right) // 2
            val = mid*mid
            if (val == num):
                return True
            elif (val > num):
                right = mid-1
            else:
                left = mid+1
        return False