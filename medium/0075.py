# https://leetcode.com/problems/sort-colors/

from typing import Dict, List

class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    bucket:Dict[int, int] = {0:0, 1:0, 2:0}
    for num in nums:
      bucket[num] += 1
    
    num_index = 0
    val_index = 0
    n = len(nums)
    while num_index < n:
      while num_index < n and bucket[val_index] > 0:
        nums[num_index] = val_index
        num_index += 1
        bucket[val_index] -= 1
      val_index += 1
