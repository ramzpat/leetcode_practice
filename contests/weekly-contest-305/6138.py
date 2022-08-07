# https://leetcode.com/contest/weekly-contest-305/problems/longest-ideal-subsequence/

from collections import defaultdict
from typing import Dict

class Solution:
  def longestIdealString(self, s: str, k: int) -> int:
    idealCnt:Dict[int, int] = defaultdict(lambda:0)
    n = len(s)
    maxIdeal = 0
    for i in range(n):
      maxCnt = 0 
      strVal = ord(s[i])-97
      for j in range(max(0, strVal-k), min(26, strVal + k + 1)):
        maxCnt = max(maxCnt, idealCnt[j])
      idealCnt[strVal] = maxCnt + 1
      maxIdeal = max(maxIdeal, idealCnt[strVal])
    return maxIdeal
    

# "acfgbd"
# 2
# s = Solution()
# print(s.longestIdealString("acfgbd", 2))

# "azaza"
# 25
# Expect 5
s = Solution()
print(s.longestIdealString("azaza", 25))