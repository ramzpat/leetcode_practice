# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    start, end = 0, 0 
    current_sum = 0 
    min_lenght = float('inf')
    n = len(nums)
    while end < n:
      current_sum += nums[end]
      end += 1

      while start < end and (end - start >= min_lenght or current_sum >= target):
        if current_sum >= target:
          min_lenght = min(min_lenght, end - start)
        current_sum -= nums[start]
        start += 1

    return 0 if min_lenght == float('inf') else min_lenght