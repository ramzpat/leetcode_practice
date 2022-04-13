# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        val = self.stack[0]
        self.stack = self.stack[1:]
        return val

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (len(self.stack) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()