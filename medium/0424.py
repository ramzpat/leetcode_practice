# https://leetcode.com/problems/longest-repeating-character-replacement/
# Solution: https://leetcode.com/problems/longest-repeating-character-replacement/discuss/363071/Simple-Python-two-pointer-solution

from typing import Dict


class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    i = 0 
    n = len(s)
    max_len = 0
    cntS:Dict[str, int] = {}
    left = 0
    for right in range(n):
      cntS[s[right]] = cntS.get(s[right], 0) + 1
      while (right - (left - 1)) - max(cntS.values()) > k: 
        cntS[s[left]] -= 1 
        left += 1
      max_len = max(max_len, (right - (left - 1)))
    return max_len

# Test 
s = Solution()
# Input: s = "ABAB", k = 2
# Output: 4
print(s.characterReplacement(s = "ABAB", k = 2))

# Input: s = "AABABBA", k = 1
# Output: 4
print(s.characterReplacement(s = "AABABBA", k = 1))