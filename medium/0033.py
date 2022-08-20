# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    
    # find the 0-index in the rotated array 
    index = n - 1
    left, right = 0, n - 1
    while (left < right):
      mid = (left + right) // 2
      if nums[mid] > nums[right]:
        left = mid + 1
      elif nums[mid] < nums[right]:
        right = mid
    index = left
    # find target's index
    left, right = 0, n - 1
    while left <= right:
      mid = (left + right) // 2
      mid_val = nums[(index + mid) % n]
      if mid_val == target:
        return (index + mid) % n
      elif mid_val < target:
        left = mid + 1
      else:
        right = mid - 1
    return -1 