# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = (0, len(nums)-1)
        while (left <= right):
            mid = (left+right)/2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                right = mid - 1
            else: 
                left = mid + 1
        return mid+1 if nums[mid] < target else mid

s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5))
print(s.searchInsert(nums = [1,3,5,6], target = 2))
print(s.searchInsert(nums = [1,3,5,6], target = 7))