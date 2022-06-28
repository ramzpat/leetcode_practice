# https://leetcode.com/problems/logger-rate-limiter/

from collections import defaultdict
from re import M
from typing import Dict

class Logger:

  def __init__(self):
    self.msg_time:Dict[str, int] = defaultdict(lambda: 0)

  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    if  timestamp >= self.msg_time[message]:
      self.msg_time[message] = timestamp + 10
      return True 
    return False 


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)