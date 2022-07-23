# https://leetcode.com/problems/minimum-knight-moves/

from typing import List, Tuple


class Solution:
  def minKnightMoves(self, x: int, y: int) -> int:
    
    q_move:List[Tuple[Tuple[int, int], int]] = []
    q_move.append(((0, 0), 0))
    visited = set((0, 0))
    
    while(len(q_move) > 0):
      (position, cnt) = q_move.pop(0)
      current_x, current_y = position[0], position[1]

      if current_x == x and current_y == y:
        return cnt
      else: 
        for (adjust_x, adjust_y) in [ (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2) ]:
          new_x = current_x + adjust_x
          new_y = current_y + adjust_y
          if (new_x, new_y) not in visited: 
            visited.add((new_x, new_y))
            q_move.append(((new_x, new_y), cnt+1))
    