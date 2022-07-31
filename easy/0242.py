# https://leetcode.com/problems/valid-anagram/

from typing import Counter


class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    cnt_s = Counter(s)
    cnt_t = Counter(t)
    return cnt_s.keys() == cnt_t.keys() and all(cnt_s[s] == cnt_t[s] for s in cnt_s.keys())

# Test 
s = Solution()
print(s.isAnagram("abva", "aabv"))