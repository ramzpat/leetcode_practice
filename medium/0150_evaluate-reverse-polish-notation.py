# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        sum = 0
        
        for token in tokens: 
            if token == "+":
                ele_a = num_stack.pop()
                ele_b = num_stack.pop()
                num_stack.append(ele_a + ele_b)
            elif token == "-":
                ele_a = num_stack.pop()
                ele_b = num_stack.pop()
                num_stack.append(ele_b - ele_a)
            elif token == "*":
                ele_a = num_stack.pop()
                ele_b = num_stack.pop()
                num_stack.append(ele_a * ele_b)
            elif token == "/":
                ele_a = num_stack.pop()
                ele_b = num_stack.pop()
                num_stack.append(int(ele_b / ele_a))
            else:
                num_stack.append(int(token))
        return num_stack.pop()

s = Solution()
ret = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(ret)