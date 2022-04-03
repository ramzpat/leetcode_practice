# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    target = 1
    if num == target:
        return 0
    if num > target:
        return 1
    else:
        return -1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        (left, right) = (1, n+1)
        while(left <= right):
            mid = (left+right)/2
            if (guess(mid) == 0):
                return mid
            
            if (guess(mid) == 1):
                right = mid
            else:
                left = mid+1
        return -1

s = Solution()
print(s.guessNumber(2))