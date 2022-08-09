# https://leetcode.com/problems/number-of-islands/

from typing import List, Set, Tuple 

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    visited:Set[Tuple[int, int]] = set() 
    stk:List[Tuple[int, int]] = []

    cnt = 0 
    n, m = len(grid), len(grid[0])
    for i in range(n):
      for j in range(m):
        if grid[i][j] == '1' and (i, j) not in visited:
          stk.append((i, j))
          while len(stk) > 0:
            (a, b) = stk.pop()
            if a >= 0 and a < n and b >= 0 and b < m and grid[a][b] == '1' and (a, b) not in visited:
              visited.add((a, b))
              for (k, l) in [(1, 0), (0, 1), (-1, 0), (0, -1) ]:
                stk.append(a + k, b + l)
          cnt += 1 
    return cnt 

# Test 
# [1]