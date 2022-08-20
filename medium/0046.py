# https://leetcode.com/problems/permutations/

from collections import defaultdict
from typing import Dict, List


class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    def dfs_recursive_permute(nums:List[int]) -> List[List[int]]:
      solution = []
      n = len(nums)
      visited:Dict[int, bool] = defaultdict(lambda: False)
      def dfs(comb:List[int] = [], len:int = 0):
        nonlocal n 
        if len == n:
          solution.append(comb)
          return 
        for i in nums:
          if visited[i] == False:
            visited[i] = True 
            dfs(comb + [i], len + 1)
            visited[i] = False
      dfs()
      return solution
    return dfs_recursive_permute(nums)