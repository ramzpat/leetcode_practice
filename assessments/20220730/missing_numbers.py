# https://leetcode.com/problems/missing-number/

from typing import Dict, List, Set

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    # If we have the nums from 0 to n, the summation of all numbers should be '(0 + n)*(n+1) // 2' 
    # sum([0, 1, 2, 3]) = (0 + 3) / 2 * 4 = 6
    sum = ((0+n)*(n+1))//2
    for n in nums:
      sum -= n
    return sum 

# Test 
s = Solution()

print(s.missingNumber(nums = [0, 1, 2]))

print(s.missingNumber(nums = [0, 1, 3]))
print(s.missingNumber(nums = [2, 1, 3]))