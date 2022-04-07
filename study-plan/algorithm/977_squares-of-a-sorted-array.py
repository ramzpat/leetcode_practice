# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg_val = []
        pos_val = []
        i = 0
        j = 0

        while (i < len(nums)) and (nums[i] < 0):
            neg_val.append(nums[i]**2)
            i += 1
        j = i-1
        while (i < len(nums) or j >= 0):
            if (i >= len(nums)) or (j >= 0 and neg_val[j] < nums[i]**2):
                pos_val.append(neg_val[j])
                j -= 1
            else:
                pos_val.append(nums[i]**2)
                i += 1

        return pos_val