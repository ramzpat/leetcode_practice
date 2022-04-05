# https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m*n-1
        while (left <= right):
            mid = (left+right)//2
            val = matrix[mid//n][mid%n]
            if (val == target):
                return True
            elif (val > target):
                right = mid - 1
            else:
                left = mid + 1

        return False