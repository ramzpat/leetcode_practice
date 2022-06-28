# https://leetcode.com/problems/maximum-split-of-positive-even-integers/

from collections import defaultdict
from typing import List, Dict, final

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        i = 2
        ans = []
        if finalSum %2 == 0:
          while i <= finalSum:
            ans.append(i)
            finalSum -= i
            i += 2
          ans[-1] += finalSum
        return ans

s = Solution()
ret = s.maximumEvenSplit(8)
print(ret)