# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def __init__(self):
        self.queue = collections.deque()
            
    def read(self, buf, n):
        total = 0
        bytes = 4
        while bytes>=4:
            buf4 = [""]*4
            read4(buf4)
            self.queue.extend([i for i in buf4 if i])
            bytes = min(len(self.queue),n-total)
            for i in xrange(bytes):
                buf[total] = self.queue.popleft()
                total += 1
        return total
