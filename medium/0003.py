# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import Dict


class Solution:
  def lengthOfLongestSubstringRT(self, s: str) -> int:
    # Brute force
    def check(start:int, end:int) -> bool:
      cntS = set()
      for i in range(start, end+1):
        if s[i] in cntS:
          return False 
        cntS.add(s[i])
      return True 

    n = len(s)
    ans = 0
    for i in range(n):
      for j in range(i, n):
        if check(i, j):
          ans = max(ans, j-i+1)
    return ans 

  def lengthOfLongestSubstring(self, s: str) -> int:
    last_position:Dict[str, int] = {}

    n = len(s)
    max_len = 0
    i = 0
    for j in range(n):
      if s[j] in last_position:
        i = max(i, last_position[s[j]] + 1)
      max_len = max(max_len, j-i+1)
      last_position[s[j]] = j
    return max_len

s = Solution()
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
print(s.lengthOfLongestSubstring(s = "abcabcbb"))
print(s.lengthOfLongestSubstring(s = "b"))