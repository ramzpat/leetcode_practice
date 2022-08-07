# https://leetcode.com/contest/weekly-contest-305/problems/number-of-arithmetic-triplets/

from typing import List


class Solution:
  def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    n = len(nums)
    cnt = 0  
    for i in range(n):
      for j in range(i+1, n):
        if nums[j] - nums[i] == diff:
          for k in range(j+1, n):
            if nums[k] - nums[j] == diff:
              cnt += 1
              break
    return cnt 

s = Solution()
