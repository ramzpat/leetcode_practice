# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List

# The number of intervals is around 10^5. O(n^2) would be possible, isn't it? 
# The interval value is in the range of integers (negative is possible)

# First, we need to sort the intervals using the starting point O(n log(n))
# 1. DP may be needed 
# 2. Binary search 

# Binary search for the maximum end interval 
# DP store the maximum number of non-overlapping intervals 
# sorted array (start, end, max_count)
# Given [s_i, e_i, cnt_i], binary search for e_j where e_j <= s_i so that cnt_i = cnt_j + 1
# If we cannot find it, cnt_i = 1

class Solution:
  # O(n^2): Time limit exceed
  def TLE_eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    sorted_interval = sorted(intervals, key=lambda x: x[1])
    n = len(sorted_interval)
    dp = [1]
    max_cnt = 1
    for i in range(1, n):
      s_i, e_i = sorted_interval[i]
      dp.append(1)
      for j in range(i-1, -1, -1):
        s_j, e_j = sorted_interval[j]
        if e_j <= s_i:
          dp[i] = max(dp[i], dp[j] + 1)
      max_cnt = max(dp[i], max_cnt)
    return n - max_cnt 

  # Heuristic approach 
  # Idea: 
  # - Sort the intervals based on their end times 
  # - When the end times are sorted, we could check if the starting time s_i can be the next for [s_j, e_j] where e_j <= s_i. 
  # - As the end time e_j is sorted, we tend to choose the smallest interval where 
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # [1,4], [2, 10], [2, 5], [4, 6]
    # end               : 4, 4, 4, 6
    # removing_cnt      : 0, 1, 2, 2 
    
    # sort the interval using end
    sorted_interval = sorted(intervals, key=lambda x: x[1])
    n = len(sorted_interval)
    last_end = None
    remove_cnt = 0
    for [s, e] in sorted_interval:
      if last_end == None or s >= last_end:
        # We can have interval [s, e] be the next interval for [ ..., last_end] or there is no last_end 
        # So, we update the last end to be [..., e]
        last_end = e
      else: 
        # We cannot have this interval [s, e] be the next interval.
        # So, we should remove this interval 
        remove_cnt += 1
    return remove_cnt
      