class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        mat = [[0]*n for i in xrange(n)]
        
        start = 0
        end = n-1
        x = 1
        
        while start<end:
            for i in xrange(end-start):
                mat[start][start+i] = x
                x += 1
            for i in xrange(end-start):
                mat[start+i][end] = x
                x += 1
            for i in xrange(end-start):
                mat[end][end-i] = x
                x += 1
            for i in xrange(end-start):
                mat[end-i][start] = x
                x += 1
            start += 1
            end -= 1
        
        if start==end:
            mat[start][start] = x
        
        return mat