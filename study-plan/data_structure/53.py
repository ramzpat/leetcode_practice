# https://leetcode.com/problems/maximum-subarray/
# TODO: Use divide and conquer

class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0] 
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i]) 
            if (current_sum > max_sum):
                max_sum = current_sum
        return max_sum

s = Solution()
# ret = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# ret = s.maxSubArray([-2,-1])
ret = s.maxSubArray([1])
print(ret)