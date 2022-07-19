# https://leetcode.com/problems/sentence-screen-fitting/

class Solution:
  def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
    s = ' '.join(sentence) + ' '
    start = 0
    len_s = len(s)
    for _ in range(rows):
      start += cols - 1  # move the index to the end of column

      if s[start % len_s] == ' ':
        # Case 1: the location of string s is ' '
        # We should consider the next character/word for the next row
        start += 1
      elif s[(start+1) % len_s] == ' ':
        # Case 2: the location is already at the end of last word in s
        # We should start from the next 2 character 
        start += 2
      else:
        # Case 3: We are at a character in the string
        # We should go back until we find a space
        while start > 0 and s[(start-1) % len_s] != ' ':
          start -= 1
    # return the numbers that every words appear on the screen
    return start//len_s
      