# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stack.append(p)
            else:
                if (len(stack) == 0):
                    return False
                t = stack.pop()
                if t == '(' and p != ')':
                    return False
                if t == '[' and p != ']':
                    return False
                if t == '{' and p != '}':
                    return False
        return (len(stack) == 0)

s = Solution()
print(s.isValid("()"))