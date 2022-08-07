# https://leetcode.com/contest/weekly-contest-305/problems/check-if-there-is-a-valid-partition-for-the-array/

from typing import List


class Solution:
  def validPartition(self, nums: List[int]) -> bool:
    n = len(nums)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(2, n+1):
      # condition 1
      dp[i] = (nums[i-1] == nums[i-2] and dp[i-2]) 
      # condition 2
      dp[i] = dp[i] or (i > 2 and nums[i-1] == nums[i-2] and nums[i-2] == nums[i-3] and dp[i-3])
      # condition 3
      dp[i] = dp[i] or (i > 2 and nums[i-1] - nums[i-2] == 1 and nums[i-2] - nums[i-3] == 1 and dp[i-3])
    return dp[n] 

s = Solution()
print(s.validPartition(nums = [1,1,1,2]))