# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    prod_left = [1] * n
    prod_right = [1] * n
    for i in range(1, n):
      prod_left[i] = prod_left[i-1]*nums[i-1]
      
    for i in range(n-2, -1, -1):
      prod_right[i] = prod_right[i+1]*nums[i+1]
      
    return [x * y for x, y in zip(prod_left, prod_right)]
