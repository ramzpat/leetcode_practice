# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict
from typing import Dict


class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    last_pos:Dict[str, int] = defaultdict(lambda: -1)
    max_len = 0
    last_str_begin = 0
    for i, c in enumerate(s):
      last_str_begin = max(last_str_begin, last_pos[c] + 1) 
      max_len = max(max_len, i - last_str_begin + 1)
      last_pos[c] = i        
    return max_len 
