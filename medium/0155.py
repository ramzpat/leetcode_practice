# https://leetcode.com/problems/min-stack/

from typing import List, Tuple


class MinStack:

    def __init__(self):
      # Value: (value, current_min)
      self.min_stack:List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
      min_val = self.getMin()
      self.min_stack.append(val, min(min_val, val))  

    def pop(self) -> None:
      self.min_stack.pop()

    def top(self) -> int:
      top_val, _ = self.min_stack[-1]
      return top_val

    def getMin(self) -> int:
      _, min_val = self.min_stack[-1]
      return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()