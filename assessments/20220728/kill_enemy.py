
# Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.
# https://leetcode.com/problems/bomb-enemy/
from typing import List, Set, Tuple


class Solution:
  def maxKilledEnemies(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    cntKill:List[List[int]] = [ [0]*n for _ in range(m) ]

    # left -> right:
    for i in range(m):
      cnt = 0
      for j in range(n):
        if grid[i][j] == "W":
          cnt = 0
        elif grid[i][j] == "E":
          cnt += 1
        elif grid[i][j] == "0":
          cntKill[i][j] = cnt

    # right -> left:
    for i in range(m):
      cnt = 0
      for j in range(n-1, -1, -1):
        if grid[i][j] == "W":
          cnt = 0
        elif grid[i][j] == "E":
          cnt += 1
        elif grid[i][j] == "0":
          cntKill[i][j] += cnt
 
    # up -> down 
    for j in range(n):
      cnt = 0
      for i in range(m):
        if grid[i][j] == "W":
          cnt = 0
        elif grid[i][j] == "E":
          cnt += 1
        elif grid[i][j] == "0":
          cntKill[i][j] += cnt

    # down -> up 
    for j in range(n):
      cnt = 0
      for i in range(m-1, -1, -1):
        if grid[i][j] == "W":
          cnt = 0
        elif grid[i][j] == "E":
          cnt += 1
        elif grid[i][j] == "0":
          cntKill[i][j] += cnt
    return max([cntKill[i][j] for j in range(n) for i in range(m)])


# Test 
# Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# Output: 3

s = Solution()
print(s.maxKilledEnemies(grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))

# Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
# Output: 1

print(s.maxKilledEnemies(grid = [["W","W","W"],["0","0","0"],["E","E","E"]]))

