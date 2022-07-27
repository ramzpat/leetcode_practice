# https://leetcode.com/contest/weekly-contest-303/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
          if c in seen:
            return c 
          seen.add(c)
