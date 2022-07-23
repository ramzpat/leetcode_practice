# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

from collections import defaultdict
from typing import Dict, List


class Solution:
  def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
    name_t = str
    time_str_t = str
    time_num_t = int
    records:Dict[name_t, List[time_num_t]] = defaultdict(list)

    def convertTime(time_str:time_str_t) -> time_num_t:
      [hr, min] = time_str.split(":")
      return int(hr) * 60 + int(min)
    
    for i in range(len(keyName)):
      records[keyName[i]].append(convertTime(keyTime[i]))
    
    alert = []
    for name in records.keys():
      records[name] = sorted(records[name])
      for i in range(2, len(records[name])):
        time_1 = records[name][i-2]
        time_2 = records[name][i-1]
        time_3 = records[name][i]
        if time_2 - time_1 <= 60 and time_3 - time_1 <= 60 :
          alert.append(name)
          break 
    return sorted(alert)

s = Solution()
print(s.alertNames(keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))