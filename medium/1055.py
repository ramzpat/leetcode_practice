# https://leetcode.com/problems/shortest-way-to-form-string/

class Solution:
  def shortestWay(self, source: str, target: str) -> int:
    s_i = 0
    t_i = 0 
    n = len(source)
    m = len(target)
    cnt = 0
    while t_i < m:
      # Reset s_i to search again 
      s_i = 0

      # Search for source[s_i] that match target[t_i]
      while (s_i < n and source[s_i] != target[t_i]):
        s_i += 1

      if s_i == n:
        return -1

      # Move on
      while(t_i < m and s_i < n):
        if source[s_i] == target[t_i]:
          t_i += 1
        s_i += 1 
      
      cnt += 1
    return cnt 