# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    
    def loop_maxSubArray(nums: List[int]) -> int:
      n = len(nums)
      max_val = nums[0]
      for i in range(n):
        current_sum = 0
        for j in range(i, n):
          current_sum += nums[j]
          max_val = max(current_sum, max_val)
      return max_val 

    def dp_maxSubArray(nums: List[int]) -> int:
      max_val = nums[0]
      current_sum = nums[0]
      for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_val = max(max_val, current_sum)
      return max_val 
    
    return loop_maxSubArray(nums)