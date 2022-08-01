# https://leetcode.com/problems/group-anagrams/

from collections import Counter, defaultdict
from typing import Dict, List


class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    grp:Dict[str, List[str]] = defaultdict(list)
    for word in strs:
      grp[str(sorted(word))].append(word)
    return [grp[work] for work in grp]

s = Solution()
print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
      