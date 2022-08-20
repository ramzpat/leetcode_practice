# https://leetcode.com/problems/last-stone-weight-ii/

from typing import List


class Solution:
  def lastStoneWeightII(self, stones: List[int]) -> int:
    def knapsack(stones:List[int]) -> int:
      total_sum = sum(stones)
      maxW = total_sum // 2 
      dp:List[List[int]] = [[0] * (maxW + 1) for _ in range(len(stones)+1)]
      
      for i, s in enumerate(stones):
        for w in range(min(s,maxW+1)):
          dp[i+1][w] = dp[i][w]
        for w in range(s, maxW+1):
          dp[i+1][w] = max(dp[i][w], dp[i][w-s] + s)  
      max_half_sum = dp[len(stones)][maxW]
      another_half_sum = (total_sum - max_half_sum)
      return (another_half_sum - max_half_sum)
    return knapsack(stones)