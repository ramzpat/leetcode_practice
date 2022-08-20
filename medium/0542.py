# https://leetcode.com/problems/01-matrix/

from collections import deque
from typing import List

class Solution:
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    ans:List[List[int]] = [ [0] * n  for _ in range(m)]
    q = deque([])

    # find all 1 that has at least one 0 around it 
    for i in range(m):
      for j in range(n):
        if mat[i][j] == 1 and any( mat[i+k][j+l] == 0 for (k, l) in [(0,1), (1,0), (-1, 0), (0, -1)] if i + k >= 0 and i + k < m and j + l >= 0 and j + l < n):
          q.append((i, j, 1))

    visited = set()
    while len(q) > 0:
      (x, y, cnt) = q.popleft()
      if x >= 0 and x < m and y >= 0 and y < n and mat[x][y] == 1 and (x,y) not in visited:
        visited.add((x, y))
        ans[x][y] = cnt

        # add more 
        for (k, l) in [(0,1), (1,0), (-1, 0), (0, -1)]: 
          if x + k >= 0 and x + k < m and y + l >= 0 and y + l < n:
            if mat[x+k][y+l] == 1:
              q.append((x+k, y+l, cnt+1))

    return ans 


      