# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt = {}
        if len(s) != len(t):
            return False 
        for e in s:
            if not( e in cnt):
                cnt[e] = 1
            else:
                cnt[e] += 1
        for e in t:
            if not( e in cnt):
                return False 
            elif (cnt[e] <= 0):
                return False
            else:
                cnt[e] -= 1
        return True 