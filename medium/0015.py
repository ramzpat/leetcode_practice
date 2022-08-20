# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)

    i = 0
    n = len(nums)
    ans = []
    while i < n:
      j = i + 1
      k = n - 1
      while j < k:
        if nums[i] + nums[j] + nums[k] == 0:
          ans.append([nums[i], nums[j], nums[k]])
          j += 1
          while j < k and nums[j-1] == nums[j]:
            j += 1
        elif nums[j] + nums[k] < -nums[i]:
          j += 1
          while j < k and nums[j-1] == nums[j]:
            j += 1
        elif nums[j] + nums[k] > -nums[i]:
          k -= 1
          while j < k and nums[k] == nums[k+1]:
            k -= 1
      i += 1
      while i < n and nums[i-1] == nums[i]:
        i += 1
    return ans