# https://leetcode.com/problems/longest-string-chain/

from collections import defaultdict


class Solution:
  def longestStrChain(self, words: List[str]) -> int:
    dp = defaultdict(lambda: 0)
    for w in sorted(words, key=len):
      dp[w] = max( dp[w[:i] + w[i+1:]] + 1 for i in range(0,len(w)))
    return max(dp.values())