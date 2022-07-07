# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List 

class Solution:
  def maxScore(self, cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    
    # Sum the cards from right first
    tmp_sum = sum(v for v in cardPoints[n-k:])
    # Assign the maximum value 
    maxSum = tmp_sum
    # Assign the index of sum cardPoints[n-k:]
    j = n-k
    for i in range(0, min(n, k)):
      # Subtract the index [j+i] and add index [i]
      tmp_sum = tmp_sum - cardPoints[j+i] + cardPoints[i]
      # Update maximum value
      maxSum = max(tmp_sum, maxSum)

    return maxSum


s = Solution()
print(s.maxScore([96,90,41,82,39,74,64,50,30], 8)) # 536