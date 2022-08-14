# https://leetcode.com/contest/weekly-contest-306/problems/largest-local-values-in-a-matrix/
from collections import defaultdict
from typing import Dict, List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal:List[List[int]] = [[0] * (n-2) for _ in range(n-2)]

        for i in range(n-2):
          for j in range(n-2):
            for k_i in range(0, 3):
              for k_j in range(0, 3):
                index_i = i + k_i
                index_j = j + k_j
                if index_i >= 0 and index_i < n and index_j >= 0 and index_j < n:
                  maxLocal[i][j] = max(grid[index_i][index_j], maxLocal[i][j]) 
        
        return maxLocal