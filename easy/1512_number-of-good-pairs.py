# https://leetcode.com/problems/number-of-good-pairs/

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        sum = 0
        for i in range(0, len(nums)):
            if (nums[i] in seen):
                sum = sum + seen[nums[i]]
            else:
                seen[nums[i]] = 0
            seen[nums[i]] = seen[nums[i]] + 1
        return sum