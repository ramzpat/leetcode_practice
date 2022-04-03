# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 1, len(arr)-1
        while(left <= right):
            i = (left+right)/2
            if (arr[i] > arr[i-1]) and (arr[i] > arr[i+1]):
                return i
            elif arr[i] > arr[i-1]:
                left = i+1
            else:
                right = i-1


