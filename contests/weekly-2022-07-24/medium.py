# https://leetcode.com/contest/weekly-contest-303/problems/equal-row-and-column-pairs/
# https://leetcode.com/problems/equal-row-and-column-pairs/

from collections import defaultdict
from typing import Dict, List

class Solution:
  def equalPairs(self, grid: List[List[int]]) -> int:
    hashRow:Dict[int, List[int]] = defaultdict(list)

    def hashVal(l:List[int]) -> int:
      mod_val = 10**5
      val = 0
      for n in l:
        val = (val * 256 + val)%mod_val
      return val

    for i, row in enumerate(grid):
      hashRow[hashVal(row)].append(i)
    
    n = len(grid)
    cnt = 0
    for c in range(n):
      column = [grid[r][c] for r in range(n)]
      hVal = hashVal(column)
      if hVal in hashRow:
        for l in hashRow.get(hVal, []):
          if all(grid[l][i] == grid[i][c] for i in range(n)):
            cnt += 1
    return cnt

s = Solution()
print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))