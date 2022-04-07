# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = {}
        for index in range(0, len(s)):
            if not (s[index] in cnt):
                cnt[s[index]] = 1
            else:
                cnt[s[index]] = 2
        for index in range(0, len(s)):
            if cnt[s[index]] == 1:
                return index 
        return -1