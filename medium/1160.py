# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from typing import Counter, List

class Solution:
  def countCharacters(self, words: List[str], chars: str) -> int:
    cntChars:Counter = Counter(chars)
    cnt = 0
    for w in words:
      cntW:Counter = Counter(w)
      if all(cntW[c] <= cntChars[c] for c in cntW):
        cnt += len(w)
    return cnt
        