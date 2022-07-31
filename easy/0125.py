# https://leetcode.com/problems/valid-palindrome/

from cgitb import small


class Solution:
  def isPalindrome(self, s: str) -> bool:
    # clean the string
    cleaned_s = ""
    for char in s:
      small_char = char.lower()
      if (ord(small_char) >= ord('a') and ord(small_char) <= ord('z')) or (ord(small_char) >= ord('0') and ord(small_char) <= ord('9')):
        cleaned_s += small_char
    # Check if the cleaned string is palindrom
    n = len(cleaned_s)
    for i in range(n//2):
      if cleaned_s[i] != cleaned_s[n-1-i]:
        return False
    return True  

# Test
s = Solution()
# print(s.isPalindrome("aba"))
# print(s.isPalindrome("a/,##ba a ba"))
# print(s.isPalindrome("abaabsaa"))
print(s.isPalindrome("0P"))