# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index in range(0, len(nums)):
            remain = target - nums[index]
            if (remain in seen):
                return [seen[remain], index]
            seen[nums[index]] = index