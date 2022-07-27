# https://leetcode.com/problems/majority-element/

from typing import List
# https://leetcode.com/problems/majority-element/


class Solution:

  def majorityElement(self, nums: List[int]) -> int:
    # https://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html
    # https://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html
    major = nums[0]
    count = 1
    for num in nums[1:]:
      if count == 0:
        major = num
        count = 1
      elif num == major:
        count += 1
      else:
        count -= 1
    return major


# Test 
