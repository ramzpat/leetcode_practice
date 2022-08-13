# https://leetcode.com/problems/meeting-rooms/

from typing import List

class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    # We just need to ensure the intervals are not overlapping 
    intervals.sort(key=lambda x: x[0])
    for i, [s, e] in enumerate(intervals[1:]):
      _, prev_e = intervals[i]
      if s < prev_e:
        return False 
    return True 