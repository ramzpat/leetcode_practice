# https://leetcode.com/problems/rotate-array/
# Could you do it in-place with O(1) extra space?

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # reverse [0:(n-k)]
        left, right = 0, (n-k)-1
        tmp = 0
        while(left < right):
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1
        # reverse [(n-k), n]
        left, right = (n-k), n-1
        while(left < right):
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1
        # reverse [0:n]
        left, right = 0, n-1
        while(left < right):
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1