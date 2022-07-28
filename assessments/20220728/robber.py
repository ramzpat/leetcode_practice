# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.


# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

from typing import List


class Solution:
  def rob(self, nums: List[int]) -> int:
    n:int = len(nums)
    sum_nums:List[int] = [0]*(n+1)  # Best summation? 
    sum_nums[1] = nums[0]
    for i in range(2, n+1):
      sum_nums[i] = max(sum_nums[i-1], sum_nums[i-2] + nums[i-1])
    return sum_nums[n]

# Test 
s = Solution()
print(s.rob(nums = [1,2,3,1]))
print(s.rob(nums = [2,7,9,3,1]))


print(s.rob(nums = [2]))

print(s.rob(nums = [2,0,2])) # 4
print(s.rob(nums = [2,0,2,5])) # 7
