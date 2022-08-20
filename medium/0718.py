# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

from typing import List

class Solution:
  def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    m = len(nums2)
    dp:List[List[int]] = [ [0]*(m+1) for _ in range(n+1) ]
    max_len = 0 
    for i in range(1, n+1):
      for j in range(1, m+1):
        if nums1[i-1] == nums2[j-1]:
          dp[i][j] = dp[i-1][j-1] + 1
          max_len = max(max_len, dp[i][j])
    return max_len 

