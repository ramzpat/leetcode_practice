# https://leetcode.com/contest/weekly-contest-306/problems/node-with-highest-edge-score/

from collections import defaultdict
from typing import Dict, List


class Solution:
  def edgeScore(self, edges: List[int]) -> int:
    edgeScore:Dict[int, int] = defaultdict(lambda: 0)
    highestScore = 0 
    index = len(edges)
    for node, target in enumerate(edges):
      edgeScore[target] += node
      if (highestScore == edgeScore[target] and index > target) or highestScore < edgeScore[target]  :
        highestScore = edgeScore[target]
        index = target 
      
        
    return index