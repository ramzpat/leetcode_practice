# https://leetcode.com/problems/two-sum/

from collections import defaultdict
from typing import Dict, List


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen:Dict[int, int] = defaultdict(lambda: -1)
    for i, n in enumerate(nums):
      if seen[target - n] != -1:
        return [i, seen[target - n]]
      seen[n] = i