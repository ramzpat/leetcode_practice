# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
  def longestPalindrome(self, s: str) -> str:
    n = len(s)
    def find_palin(l:int, r:int):
      while(l >= 0 and r < n and s[l] == s[r]):
        l -= 1
        r += 1
      return s[l+1:r]
    ans = ""
    for i in range(0, n):
      tmp1 = find_palin(i, i)
      if len(tmp1) > len(ans):
        ans = tmp1
      tmp1 = find_palin(i, i+1)
      if len(tmp1) > len(ans):
        ans = tmp1
    return ans

s = Solution()
print(s.longestPalindrome("cbbd"))