from collections import defaultdict
from typing import Dict, List


class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    bucket:Dict[int, int] = defaultdict(lambda: 0)
    max_w_stone = 0
    min_w_stone = 101
    for s in stones:
      bucket[s] += 1
      max_w_stone = max(max_w_stone, s)
    
    i = max_w_stone
    # O(100) = O(1) because we use the pointer to indicate the location to move next
    while i >= 1: 
      # Smash the same weight
      bucket[i] = bucket[i]%2
      if (bucket[i] == 0):
        i -= 1
      else:
        # find the next lower weight
        j = i-1
        while j >= 1 and bucket[j] == 0:
          j -= 1
        
        if j == 0:
          # if we cannot find the lower weight, i is the smallest value 
          return i
        else:
          # smash i and j
          bucket[i] -= 1
          bucket[j] -= 1
          bucket[i-j] += 1
          # the next weight to be considered is either j or (i-j)
          next_lower = max(j, i-j)
          i = next_lower
    return 0


# Input: stones = [31,26,33,21,40]
# Output: 5