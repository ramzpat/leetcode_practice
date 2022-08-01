# https://leetcode.com/contest/weekly-contest-304/problems/maximum-number-of-groups-entering-a-competition/
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/


from typing import List

class Solution:
  def maximumGroups(self, grades: List[int]) -> int:
    # The first condition (sum of grades) will be automatically satisfied if we sort grades.
    n = len(grades)
    k = 0
    # 1 + 2 + 3 + ... + k <= n
    while k < n:
      k += 1
      n -= k
    return k

# test 
# Input: grades = [10,6,12,7,3,5]
# Output: 3

s = Solution()
print(s.maximumGroups(grades = [10,6,12,7,3,5]))
print(s.maximumGroups(grades = [8,8]))