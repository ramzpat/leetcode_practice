# https://leetcode.com/problems/ransom-note/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt = {}
        for s in ransomNote:
            if not(s in cnt):
                cnt[s] = 1
            else:
                cnt[s] += 1

        for s in cnt:
            if (magazine.count(s) < cnt[s]):
                return False
        return True

s = Solution()
print(s.canConstruct("a", "ab"))