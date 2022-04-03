# https://leetcode.com/problems/merge-sorted-array/

#Todo: optimize the space

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        index_1 = 0
        index_2 = 0
        ret = []
        while ((index_1 < m) or (index_2 < n)):
            while ((index_1 < m) and (index_2 < n) and (nums1[index_1] <= nums2[index_2])):
                ret.append(nums1[index_1])
                index_1 = index_1 + 1
            while ((index_1 < m) and (index_2 < n) and (nums2[index_2] <= nums1[index_1])):
                ret.append(nums2[index_2])
                index_2 = index_2 + 1
            while (index_1 >= m) and (index_2 < n):
                ret.append(nums2[index_2])
                index_2 = index_2 + 1
            while (index_2 >= n) and (index_1 < m):
                ret.append(nums1[index_1])
                index_1 = index_1 + 1
        nums1[:] = ret
            
            
            
s = Solution()
nums1 = [4,5,6,0,0,0]
s.merge(nums1, m=3, nums2=[1,2,3], n=3)
print(nums1)


nums1 = [4,0,0,0,0,0]
s.merge(nums1, m=1, nums2=[1,2,3,5,6], n=5)
print(nums1)

nums1 = [1]
s.merge(nums1, m=1, nums2=[], n=0)
print(nums1)