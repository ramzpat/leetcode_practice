# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost = [cost[0], cost[1], 0]
        for i in range(2, len(cost)):
            if (min_cost[(i+1)%3] <= min_cost[(i+2)%3]):
                min_cost[i%3] = min_cost[(i+1)%3] + cost[i]
            else:
                min_cost[i%3] = min_cost[(i+2)%3] + cost[i]
        return min(min_cost[(len(cost)+1)%3], min_cost[(len(cost)+2)%3])