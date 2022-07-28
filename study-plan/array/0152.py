# https://leetcode.com/problems/maximum-product-subarray/
# https://leetcode.com/problems/maximum-product-subarray/solution/


from typing import List


class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    n = len(nums)
    max_nums:List[int] = [0] * n
    min_nums:List[int] = [0] * n
    max_val = nums[0]
    max_nums[0] = nums[0]
    min_nums[0] = nums[0]
    for i in range(1, n):
      max_nums[i] = max(nums[i], nums[i] * max_nums[i-1], nums[i] * min_nums[i-1])
      min_nums[i] = min(nums[i], nums[i] * max_nums[i-1], nums[i] * min_nums[i-1])
      max_val = max(max_val, max_nums[i])
    return max_val

# Test 
s = Solution()

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
print(s.maxProduct(nums = [2,3,-2,4]))

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
print(s.maxProduct(nums = [-2,0,-1]))
