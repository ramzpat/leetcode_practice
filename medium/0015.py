# https://leetcode.com/problems/3sum/

from typing import List, Set

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    # https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation
    
    # O(n^2)
    nums.sort()
    n = len(nums)
    ans:List[List[int]] = []
    for i in range(n):
      if i > 0 and nums[i] == nums[i-1]:
        continue

      # find the rest sum
      target_val = -nums[i]
      s, e = i+1, n-1
      while s < e: 
        if nums[s] + nums[e] == target_val:
          # Add an answer 
          ans.append([nums[i], nums[s], nums[e]])
          s += 1
          # Avoid the duplicated items 
          while (s < e and nums[s] == nums[s-1]):
            s += 1
        elif nums[s] + nums[e] < target_val:
          # find the larger value that equal target value
          s += 1
        else:
          e -= 1
    return ans 

# Test 
s = Solution()
print(s.threeSum(nums = [0,-1,1, 0, 0]))
print(s.threeSum(nums = [0, 0, 0]))
