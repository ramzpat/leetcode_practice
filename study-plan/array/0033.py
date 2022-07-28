# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Solution: https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution

from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    # There is an integer array nums sorted in ascending order (with distinct values).

    # 1 - Find the index having smallest value
    n = len(nums)
    l, r = 0, n-1
    while(l < r):
      mid = (l+r)//2
      if (nums[mid] > nums[r]):
        # The smallest area is in the right side 
        l = mid + 1
      else:
        # nums[mid] <= nums[r]  // We probably are in the sorted area. We need to find a lowest value 
        r = mid
    
    rotate_index = l
    l, r = 0, n-1
    while(l < r):
      mid = (l + r)//2
      actual_mid = (mid + rotate_index)%n
      if nums[actual_mid] == target: 
        return actual_mid
      elif nums[actual_mid] < target:
        l = mid + 1
      else:
        r = mid

    if nums[(l+rotate_index)%n] == target:
      return (l+rotate_index)%n
    return -1 

# Test 
s = Solution()

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
print(s.search(nums = [4,5,6,7,0,1,2], target = 0))

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
print(s.search(nums = [4,5,6,7,0,1,2], target = 3))

# Input: nums = [1], target = 0
# Output: -1
print(s.search(nums = [1], target = 0))

# Input: nums = [1], target = 1
# Output: 0
print(s.search(nums = [1], target = 1))