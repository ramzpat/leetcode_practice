# https://leetcode.com/problems/battleships-in-a-board/

from typing import List

class Solution:
  def countBattleships(self, board: List[List[str]]) -> int:
    m, n = len(board), len(board[0])
    cnt = 0
    
    # count horizontal, where k >= 2
    for i in range(m):
      j = 0
      while j < n-1:
        if board[i][j] == 'X' and board[i][j+1] == 'X':
          cnt += 1
          while j < n and board[i][j] == 'X':
            board[i][j] = '.'
            j += 1
        else:
          j += 1
    
    # count vertical, where k >= 1
    for j in range(n):
      i = 0
      while i < m:
        if board[i][j] == 'X':
          cnt += 1
          while i < m and board[i][j] == 'X':
            board[i][j] = '.'
            i += 1
        else:
          i += 1
    return cnt 