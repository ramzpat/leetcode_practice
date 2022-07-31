# https://leetcode.com/problems/count-and-say/

from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        def say(nums:List[int] = [1]):
            ans = []
            n = len(nums)
            currentVal = nums[n-1]
            cnt = 1
            # Time: O(n)
            for i in range(n-2, -1, -1):
                if currentVal == nums[i]:
                    cnt += 1
                else:
                    ans = [cnt, currentVal] + ans
                    currentVal = nums[i]
                    cnt = 1
            ans = [cnt, currentVal] + ans
            return ans 
        # O(n^2)
        def recur_say(k:int = n) -> List[int]:
            if k == 1:
                return [1]
            else:
                return say(recur_say(k-1))
        return "".join([str(i) for i in recur_say(n)])

# Test 
s = Solution()
for n in range(1, 30):
  print(s.countAndSay(n))