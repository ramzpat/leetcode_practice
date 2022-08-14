# https://leetcode.com/contest/weekly-contest-306/problems/construct-smallest-number-from-di-string/

from typing import List


class Solution:
  def smallestNumber(self, pattern: str) -> str:
    n = len(pattern)
    nums:List[int] = [i for i in range(1, n+2)]
    s_index = 0
    e_index = 0
    pattern += "I"
    while s_index < n+1 and e_index < n+1:
      if pattern[e_index] == 'D':
        e_index += 1
      elif pattern[e_index] == "I":
        current_num = nums[e_index]
        for i in range(s_index, e_index+1):
          nums[i] = current_num
          current_num -= 1
        s_index = e_index + 1
        e_index += 1
    return "".join([str(n) for n in nums])
