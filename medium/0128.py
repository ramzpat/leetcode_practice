# https://leetcode.com/problems/longest-consecutive-sequence/

from collections import defaultdict
from typing import Dict, List, Set


class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    # To make the time complexity O(n), we may need hashTable to remember the numbers in the unordered list 
    # Also, we keep the minimum and maximum
    # Then, find the number of consecutive numbers using a loop from [min, max+1]

    # base case
    if len(nums) == 0:
      return 0

    allValues:Set[int] = set(nums)
    max_seq = 1
    for n in allValues:
      if n - 1 not in allValues:
        # n is the smallest value in the sequence
        # then, count the lenght of this sequence 
        cnt = 1
        i = n + 1
        while i in allValues:
          cnt += 1
          i += 1
        max_seq = max(max_seq, cnt)
    return max_seq