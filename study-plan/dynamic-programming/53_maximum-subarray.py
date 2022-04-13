# https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]
        n = len(nums)
        for i in range(1, n):
            current_sum = max(nums[i], current_sum + nums[i])
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum

s = Solution()
print(s.maxSubArray([5,4,-1,7,8]))