# https://leetcode.com/problems/house-robber-ii/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_gain_left = [0]*(len(nums) + 1)
        max_gain_left[1] = nums[0]
        for i in range(2, len(nums)):
            max_gain_left[i] = max(max_gain_left[i-1], nums[i-1] + max_gain_left[i-2])
        
        max_gain_right = [0]*(len(nums) + 1)
        max_gain_right[len(nums)] = 0
        max_gain_right[len(nums)-1] = nums[-1]
        for i in range(len(nums)-2, 0, -1):
            max_gain_right[i] = max(max_gain_right[i+1], nums[i] + max_gain_right[i+2])
        print(max_gain_left, max_gain_right)
        return max(nums[0], max(max_gain_right[1], max_gain_left[len(nums)-1]))

s = Solution()

print(s.rob([1,2,3,1]))

print(s.rob([1]))
