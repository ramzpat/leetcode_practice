# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n-1
        bad_version = 0
        while(left <= right):
            version = (left + right)//2
            if (isBadVersion(version)):
                bad_version = version
                right = version - 1
            else: 
                left = version + 1
        return bad_version