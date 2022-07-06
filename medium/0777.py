# https://leetcode.com/problems/swap-adjacent-in-lr-string/

from typing import Counter


class Solution:
  def canTransform(self, start: str, end: str) -> bool:
    if start.replace('X', '') != end.replace('X', ''):
      return False
    
    n = len(start)
    startL = [i for i in range(n) if start[i] == 'L']
    endL = [i for i in range(n) if end[i] == 'L']
    
    for i, j in zip(startL, endL):
      if (j > i): 
        return False 

    startR = [i for i in range(n) if start[i] == 'R']
    endR = [i for i in range(n) if end[i] == 'R']

    for i, j in zip(startR, endR):
      if (j < i): 
        return False 
    return True 

s = Solution()
print(s.canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))
print(s.canTransform(start = "X", end = "L"))
print(s.canTransform(start = "XLXRRXXRXX", end = "LXXXXXXRRR"))
