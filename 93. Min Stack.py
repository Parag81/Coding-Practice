"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)

        if len(self.minstack) == 0:
            self.minstack.append(x)
        else:
            if x < self.minstack[-1]:
                self.minstack.append(x) 

    # @return nothing
    def pop(self):
        if not self.stack:
            return -1 

        popped = self.stack.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()


    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1 

    # @return an integer
    def getMin(self):
        if not self.stack:
            return -1 

        return self.minstack[-1]