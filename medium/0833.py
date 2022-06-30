# https://leetcode.com/problems/find-and-replace-in-string/

from heapq import heappush
from operator import itemgetter
from typing import List 

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
      replacement = sorted([(indices[i], sources[i], targets[i]) for i in range(len(indices))], key=itemgetter(0))
      new_s = ""
      max_indice = 0

      for (indice, src, tar) in replacement:
        if max_indice > indice:
          return s

        len_src = len(src)
        if src == s[indice:indice + len_src]:
          new_s = new_s + s[max_indice:indice] + tar
          max_indice = indice+len_src
      
      return new_s + s[max_indice:]

s = Solution()
print(s.findReplaceString(s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]))