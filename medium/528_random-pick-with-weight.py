# https://leetcode.com/problems/random-pick-with-weight/

import random

class Solution(object):
    weights = []
    sum_weight = []
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sum_weight = [w[0]]
        for i in range(1, len(w)):
            self.sum_weight.append(self.sum_weight[i-1] + w[i])
    
    def pickIndex(self):
        """
        :rtype: int
        """
        rand_val = random.random() * self.sum_weight[-1]
        
        # Binary search
        (left, right) = (0, len(self.sum_weight)-1)
        picked_val = 0
        while(left < right):
            mid = (left+right)/2
            if (rand_val > self.sum_weight[mid]):
                picked_val = mid + 1
                left = mid + 1
            if (rand_val < self.sum_weight[mid]):
                right = mid
        return picked_val


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

obj = Solution([1,1])
param_1 = obj.pickIndex()
print(param_1)
param_1 = obj.pickIndex()
print(param_1)
param_1 = obj.pickIndex()
print(param_1)
param_1 = obj.pickIndex()
print(param_1)
param_1 = obj.pickIndex()
print(param_1)
param_1 = obj.pickIndex()
print(param_1)