class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows==1: return s
        
        label = {i:[] for i in xrange(numRows)}
        row = 0
        incr = True
        zig = ''
        
        for i in xrange(len(s)):
            label[row].append(s[i])

            if row==0: incr = True
            if row==numRows-1: incr = False
            if incr: row += 1
            else: row -= 1

        for i in xrange(numRows):
            for c in label[i]:
                zig += c

        return zig
