# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_map = {}
        for n in nums1:
            if not(n in hash_map):
                hash_map[n] = 0
            hash_map[n] += 1

        ret_map = []
        for n in nums2:
            if (n in hash_map) and (hash_map[n] > 0):
                ret_map.append(n)
                hash_map[n] -= 1
        return ret_map

s = Solution()
ret = s.intersect(nums1 = [1,2,2,1], nums2 = [2,2])
print(ret)