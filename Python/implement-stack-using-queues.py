class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q = [collections.deque(), collections.deque()]
        self.nth = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q[self.nth].append(x)

    # @return nothing
    def pop(self):
        while len(self.q[self.nth])>1:
            self.q[1-self.nth].append(self.q[self.nth].popleft())
        self.q[self.nth].popleft()
        self.nth = 1-self.nth

    # @return an integer
    def top(self):
        return self.q[self.nth][-1]

    # @return an boolean
    def empty(self):
        return not self.q[self.nth]
