# https://leetcode.com/problems/combination-sum/

from typing import Dict, List

class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

    def dfs_solution(candidates:List[int], target:int) -> List[List[int]]:
      solution = []

      def dfs(comb:List[int], remaining_sum:int, c_index = 0):
        if remaining_sum == 0:
          solution.append(comb)
        if remaining_sum < 0:
          return
        for i in range(c_index,len(candidates)):
          if candidates[i] <= remaining_sum:
            dfs(comb + [candidates[i]], remaining_sum - candidates[i], i)
        
      dfs([], target)
      return solution

    def dp_solution(candidates:List[int], target:int) -> List[List[int]]:
      dp_sol:Dict[int, List[List[int]]] = { i:[] for i in range(target+1) }
      for c in candidates:
        if c <= target:
          dp_sol[c].append([c])
          for i in range(c+1, target+1):
            for combination in dp_sol[i-c]:
              dp_sol[i].append(combination + [c])
      return dp_sol[target]

    return dfs_solution(candidates, target)