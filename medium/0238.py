# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    dp_left = [1] * (n+2)
    dp_right = [1] * (n+2)
    ans = [1] * n
    for i in range(1, n):
      dp_left[i] = dp_left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
      dp_right[i] = dp_right[i+1] * nums[i+1]
    for i in range(0, n):
      ans[i] = dp_left[i] * dp_right[i]
    return ans 