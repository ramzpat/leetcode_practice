# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

from typing import List 

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        board_v = [ [ board[j][i] for j in range(m) ] for i in range(n)]
        alter_word = word[::-1]
        l = len(word)
        # print(board_v)
        for row in board + board_v:
          slots = ''.join(row).split('#')
          for s in slots:
            if len(s) == l:
               for w in [word, alter_word]:
                if all( s[i] == ' ' or s[i] == w[i]  for i in range(l)):
                  return True 
        return False

s = Solution()
# print(s.placeWordInCrossword(board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"))
print(s.placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"))