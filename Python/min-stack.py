class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.tracker = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if self.tracker and self.tracker[-1]<x:
            self.tracker.append(self.tracker[-1])
        else:
            self.tracker.append(x)
    # @return nothing
    def pop(self):
        self.stack.pop()
        self.tracker.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.tracker[-1]
