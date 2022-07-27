# https://leetcode.com/problems/single-number/

from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    # According to the discussion, it is better to use XOR if we want to get an Time:O(n), space:O(1) solution
    # Idea: 
    #   - 1 ^ 1 = 0
    #   - (1^1)^(2^2)^3 = 0^0^3 = 3

    result:int = nums[0]
    for val in nums[1:]:
      result ^= val
    return result 

# Test 
s = Solution()
print(s.singleNumber([2,1,1,2,3]))
print(s.singleNumber([2]))
