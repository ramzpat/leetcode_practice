# https://leetcode.com/problems/non-decreasing-array/

from typing import List

class Solution:
  def checkPossibility(self, nums: List[int]) -> bool:
    n = len(nums)
    change_cnt = 0

    # find the first position to correct 
    i = 0
    index = -1
    while i < n-1:
      if nums[i] > nums[i+1]:
        if index != -1:
          return False 
        index = i
      i += 1

    if index == -1 or index == 0 or index == n-2:
      return True
    elif index > 0 and nums[index-1] <= nums[index+1]:
      return True
    elif index < n - 2 and nums[index] <= nums[index+2]:
      return True
    
    return False