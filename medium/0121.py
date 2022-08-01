# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


from curses.ascii import SO
from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_buy = prices[0]
    n = len(prices)
    for i in range(1, n):
      max_profit = max(max_profit, prices[i] - min_buy)
      min_buy = min(min_buy, prices[i])
    return max_profit

# test 
s = Solution()

# Input: prices = [7,1,5,3,6,4]
# Output: 5
print(s.maxProfit(prices = [7,1,5,3,6,4]))

# Input: prices = [7,6,4,3,1]
# Output: 0
print(s.maxProfit(prices = [7,6,4,3,1]))


# Input: prices = [7]
# Output: 0
print(s.maxProfit(prices = [7]))


# Input: prices = [1, 2, 3, 20, 200, 0]
# Output: 199
print(s.maxProfit(prices = [1, 2, 3, 20, 200, 0]))


# Input: prices = [1, 1, 1, 1]
# Output: 0
print(s.maxProfit(prices = [1, 1, 1, 1]))
