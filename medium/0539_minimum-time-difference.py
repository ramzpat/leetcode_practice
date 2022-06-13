# https://leetcode.com/problems/minimum-time-difference/

from typing import List 

class Solution:
  def findMinDifference(self, timePoints: List[str]) -> int:    
    # Def: Convert time to min
    def to_min(time:str) -> int:
        return (60*int(time[0:2])) + int(time[3:5])

    # Convert all times 
    minutes = map(lambda time: (60*int(time[0:2]))  + int(time[3:5]) , timePoints)
    
    # Sort: min -> max so that we can compare time[a+1] - time[a] and the value will be a positive value 
    # The closest time will represent the minimum time difference
    minutes = sorted(minutes)
    # Also, we need to compare (t[0] - t[n]) for invert time 
    min_value = min((t_b - t_a)%(24*60) for t_a, t_b in zip(minutes, minutes[1:] + minutes[:1]))
    return min_value
