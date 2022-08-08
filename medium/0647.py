# https://leetcode.com/problems/palindromic-substrings/

class Solution:
  def countSubstrings(self, s: str) -> int:
    n = len(s)
    palin_count = 0

    # odd lenght 
    # Time: O(n^2)
    for i in range(n):
      for j in range(n):
        if i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
          palin_count += 1
        else:
          break 

    # even lenght
    # Time: O(n^2)
    for i in range(n):
      for j in range(n):
        if i - j >= 0 and i + 1 + j < n and s[i-j] == s[i+1+j]:
          palin_count += 1
        else:
          break 

    return palin_count

# Test case 
# 0 : a - 1
# 1 : aa - 3
# 2 : aaa - 6
# 3 : aba - 4
# 4 : abab - 6
# 5 : ababa