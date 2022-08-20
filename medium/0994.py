# https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    ans = [ [0] * n for _ in range(m) ]
    que = deque([])
    good_orange_num = 0
    
    def in_range(i:int, j:int) -> bool:
      return (i >= 0 and i < m and j >= 0 and j < n)
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1: 
          ans[i][j] = float('inf')
          good_orange_num += 1
        elif grid[i][j] == 2:
          for (x, y) in dir:
            if in_range(i+x, j+y) and grid[i+x][j+y] == 1:
              que.append((i+x, j+y, 0))
    
    visited = set()
    min_rotting_day = 0
    while len(que) > 0:
      (i, j, cnt) = que.popleft()
      if in_range(i, j) and grid[i][j] == 1 and (i, j) not in visited:
        ans[i][j] = min(ans[i][j], cnt + 1)
        min_rotting_day = max(min_rotting_day, ans[i][j])
        visited.add((i, j))
        good_orange_num -= 1
        
        # rot more 
        for (x, y) in dir:
          if in_range(i+x, j+y) and grid[i+x][j+y] == 1:
            que.append((i+x, j+y, ans[i][j]))
            
    if good_orange_num < 0:
      raise AssertionError('Something wrong')
    return min_rotting_day if (good_orange_num == 0) else -1