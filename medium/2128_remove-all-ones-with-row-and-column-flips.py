# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/
# Solution: https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1695472/Python-3-or-Simple-Explanation

class Solution:
  def removeOnes(self, grid: List[List[int]]) -> bool:
    m = len(grid)
    n = len(grid[0])
    row_orig = grid[0]
    row_flip = [1 - x for x in grid[0]]

    for row in range(1, m):
      if grid[row] != row_orig and grid[row] != row_flip:
        return False
    return True 