# https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_gain = [0, nums[0]]
        for i in range(2, len(nums)+1):
            max_gain.append(max(max_gain[i-1], nums[i-1] + max_gain[i-2]))
        print(max_gain)
        return max_gain[len(nums)]

s = Solution()
print("2")
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))

print(s.rob([2]))

print(s.rob([2, 1, 1, 2 ]))