# https://leetcode.com/contest/weekly-contest-304/problems/make-array-zero-by-subtracting-equal-amounts/

from typing import List, Set


class Solution:
  def minimumOperations(self, nums: List[int]) -> int:
    # O(n)
    nums_set:Set[int] = set(nums)

    nums_list:List[int] = sorted(list(nums_set), reverse=True)

    subtract = 0
    op_cnt = 0
    n = len(nums_list)
    # O(n^2)
    i = n-1
    while i >= 0 and len(nums_list) > 0:
      if nums_list[i] > 0:
        subtract = nums_list[i]
        nums_list.pop()
        op_cnt += 1
        for j in range(i-1, -1, -1):
          nums_list[j] -= subtract  
          # The value can be negative, but we don't need to care about it, isn't it?
      else:
        nums_list.pop()
      i -= 1

    return op_cnt

s = Solution()

# Input: nums = [1,5,0,3,5]
# Output: 3

print(s.minimumOperations(nums = [1,5,0,3,5]))
print(s.minimumOperations(nums = [0]))
print(s.minimumOperations(nums = [5,6]))
print(s.minimumOperations(nums = [5,5]))
print(s.minimumOperations(nums = [1,3,5,7,9,9]))