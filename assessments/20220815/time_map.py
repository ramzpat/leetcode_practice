from collections import defaultdict
from time import time
from typing import Dict, List, Tuple


class TimeMap:

    def __init__(self):
      self.storage:Dict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
      # timestamp will strictly increase when set is called 
      self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
      n = len(self.storage[key])
      
      # Base case 
      if n == 0:
        return ""
      
      # last_timestamp <= timestamp, O(1)
      if self.storage[key][n-1][0] <= timestamp:
        return self.storage[key][n-1][1]

      # Binary search 
      candidate_time = -1
      left, right = 0, n-1
      while (left < right):
        mid = (left + right) // 2
        if self.storage[key][mid][0] > timestamp:
          right = mid - 1
        else:
          candidate_time = left
          left = mid + 1
      if candidate_time == -1:
        return ""
      return  self.storage[key][candidate_time][1]


# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)