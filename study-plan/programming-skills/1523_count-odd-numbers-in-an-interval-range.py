# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high-low+1)/2 + (1 if high%2 != 0 and low%2 != 0 else 0)