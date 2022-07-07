# https://leetcode.com/problems/rle-iterator/

from collections import defaultdict
from heapq import heappop, heappush
from locale import currency

from typing import List

class RLEIterator:
  def __init__(self, encoding: List[int]):
    self.nums = encoding[:]
    self.index = 0 
    self.n = len(self.nums)

  def next(self, n: int) -> int:
    while(self.index < self.n):
      if n > self.nums[self.index]:
        n -= self.nums[self.index]
        self.index += 2
      else:
        self.nums[self.index] -= n
        return self.nums[self.index+1]
    return -1


# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator(encoding = [811,903,310,730,899,684,472,100,434,611])

print('---')
for [n] in [[358],[345],[154],[265],[73],[220],[138],[4],[170],[88]]:
  # print('ask:', n)
  print('got:', obj.next(n))