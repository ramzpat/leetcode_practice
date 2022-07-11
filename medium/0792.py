# https://leetcode.com/problems/number-of-matching-subsequences/

from collections import defaultdict
from typing import List 

class Solution:
  def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    word_dict = defaultdict(list)
    for w in words:
      word_dict[w[0]].append(w)
    
    cnt = 0
    for c in s:
      candidate_words = word_dict[c]
      word_dict[c] = []
      for w in candidate_words:
        if len(w) == 1:
          cnt += 1
        else:
          word_dict[w[1]].append(w[1:])
    return cnt

s = Solution()
print(s.numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))