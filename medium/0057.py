# https://leetcode.com/problems/insert-interval/

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    [new_s, new_e] = newInterval
      
    new_intervals = []
    i = 0
    n = len(intervals)
    
    # basecase
    if n == 0:
      return [newInterval]
    
    # find the place the interval can be added
    [_, e] = intervals[i]
    while(i < n and e < new_s):
      new_intervals.append(intervals[i])
      i += 1
      if i < n:
        [_, e] = intervals[i]
    
    if i == n:
      new_intervals.append([new_s, new_e])
    else:
      
      # merge the overlap
      [s, e] = intervals[i]
      new_s = min(s, new_s)
      while i < n and new_e >= s:
        new_e = max(e, new_e)
        i += 1
        if i < n:
          [s, e] = intervals[i]
      
      # insert the new interval 
      new_intervals.append([new_s, new_e])
      
      # fill the remaining
      while i < n:
        new_intervals.append(intervals[i])
        i += 1
          
    
    return new_intervals