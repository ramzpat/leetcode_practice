# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_val = 0
    last_min = prices[0]
    for p in prices[1:]:
      max_val = max(max_val, p - last_min)
      last_min = min(last_min, p)
    return max_val 