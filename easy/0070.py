# https://leetcode.com/problems/climbing-stairs/

class Solution:
  def climbStairs(self, n: int) -> int:
    ans:List[int] = [0] * (46)
    ans[1] = 1
    ans[2] = 2
    for i in range(3, n+1):
      ans[i] = ans[i-1] + ans[i-2]
    return ans[n]