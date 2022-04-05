# https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum_mat = [ [0 for c in points[0]] for r in points]
        sum_mat[0] = [c for c in points[0]]

        for r in range(1, len(points)):

            # left 
            left = [0] * len(points[r])
            left[0] = sum_mat[r-1][0]
            for c in range(1, len(points[r])):
                left[c] = max(sum_mat[r-1][c], left[c-1] - 1)
            # right 
            right = [0] * len(points[r])
            right[-1] = sum_mat[r-1][-1]
            for c in range(len(points[r]) - 2, -1, -1):
                right[c] = max(sum_mat[r-1][c], right[c+1] - 1)

            # merge
            for c in range(0, len(points[r])):
                sum_mat[r][c] = points[r][c] + max(left[c], right[c])
        
        return max(sum_mat[-1])