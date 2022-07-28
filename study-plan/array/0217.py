# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    hashN = set() 
    for n in nums:
      if n in hashN:
        return True 
      hashN.add(n)
