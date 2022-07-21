# https://leetcode.com/problems/maximum-number-of-accepted-invitations/

from typing import Dict, Set


class Solution:
  def maximumInvitations(self, grid: List[List[int]]) -> int:
    girl_t = int
    boy_t = int 
    matches:Dict[girl_t, boy_t] = {}

    num_boy, num_girl = len(grid), len(grid[0])

    def findGirl(boy_i:boy_t, asked:Set[girl_t]):
      for girl_j in range(num_girl):
        if grid[boy_i][girl_j] == 1 and girl_j not in asked:
          asked.add(girl_j) 
          # Case 1: Ask the girl if she can go with boy_i if she haven't been asked before.
          # Case 2: If not, ask the boy she is going with to ask another girl that is not in boy_i's wishlist :\
          if girl_j not in matches or findGirl(matches[girl_j], asked):
            # Hooray! boy_i can go with girl_j
            matches[girl_j] = boy_i
            return True
      # Meh... no one is going with boy_i
      return False 

    for boy_i in range(num_boy):
      findGirl(boy_i, set())

    return len(matches.keys())