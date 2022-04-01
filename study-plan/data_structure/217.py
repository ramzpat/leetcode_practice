# https://leetcode.com/problems/contains-duplicate/

from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_tab = defaultdict(int)
        for num in nums:
            if hash_tab[num]:
                return True
            hash_tab[num] = 1
            
        return False 

        