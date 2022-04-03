# https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        (left, right) = 0, len(nums)
        while (left < right):
            mid = (left+right)/2
            if (nums[mid] == target):
                return mid
            if (nums[mid] < target):
                left = mid+1
            else:
                right = mid
        return -1