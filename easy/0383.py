# https://leetcode.com/problems/ransom-note/

from collections import defaultdict
from typing import Dict


class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    mag_dict:Dict[str, int] = defaultdict(lambda:0)
    
    for char in magazine:
      mag_dict[char] += 1
    
    for char in ransomNote:
      if mag_dict[char] == 0:
        return False
      mag_dict[char] -= 0
    return True 
