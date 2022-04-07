# https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0 
        n = len(nums)
        while j < n:
            if i >= n:
                nums[j] = 0
                j += 1
            elif nums[i] != 0:
                nums[j] = nums[i]
                j += 1
                i += 1
            else:
                i += 1
            