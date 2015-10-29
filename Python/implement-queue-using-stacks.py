class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.in_stk = []
        self.out_stk = []
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.in_stk.append(x)

    # @return nothing
    def pop(self):
        self.peek()
        self.out_stk.pop()

    # @return an integer
    def peek(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    # @return an boolean
    def empty(self):
        return not self.in_stk and not self.out_stk

