# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxProfit = 0
        currentMin = prices[0]
        for i in range(1, len(prices)):
            profit_today = prices[i] - currentMin
            if profit_today > maxProfit:
                maxProfit = profit_today
            if prices[i] < currentMin:
                currentMin = prices[i]
        return maxProfit
            