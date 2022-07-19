# https://leetcode.com/problems/strings-differ-by-one-character/

from collections import defaultdict


class Solution:
  def differByOne(self, dict: List[str]) -> bool:
    # 1,000,000,007 is the smallest 10-digit prime
    mod = 1000000007
    # rabin-karp 
    hs = []
    m = len(dict[0])
    n = len(dict)
    for i, word in enumerate(dict):
      val = 0
      for j in range(m):
        val = (val*26 + (ord(word[j]) - ord('a')))%mod
      hs.append(val)
    mult = 1
    
    for j in range(m-1, -1, -1):
      seen = defaultdict(list)
      for i in range(n):
        hashVal = (hs[i] - mult * (ord(dict[i][j]) - ord('a'))) % mod 
        if hashVal in seen:
          for k in seen[hashVal]:
            cntDiff = 0
            for c, w in zip(dict[k], dict[i]):
              if c != w:
                cntDiff += 1
            if cntDiff == 1:
              return True 
        seen[hashVal].append(i)
      mult *= 26

    return False 