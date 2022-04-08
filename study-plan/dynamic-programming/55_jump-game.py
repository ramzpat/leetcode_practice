# https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = nums[0]
        i = 1
        n = len(nums)
        while ((i <= max_index) and (i < n)) and (max_index < n):
            max_jump_index = nums[i] + i
            if max_jump_index > max_index:
                max_index = max_jump_index
            i += 1
        return (max_index >= n-1)
s = Solution()
print(s.canJump([3,2,1,0,4]))
print(s.canJump([0]))