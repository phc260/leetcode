class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        stk = []
        i = sum = 0
        while i<len(height):
            if not stk or height[i]>height[stk[-1]]:
                stk.append(i)
            else:
                idx = stk.pop()
                sum = max(sum, height[idx]*(i-stk[-1]-1 if stk else i))
                i -= 1
            i += 1
        return sum
        
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        r = len(matrix)
        c = len(matrix[0])
        
        max_area = 0
        height = [0]*c
        for i in xrange(r):
            for j in xrange(c):
                height[j] = height[j]+1 if matrix[i][j]=='1' else 0
            max_area = max(max_area, self.largestRectangleArea(height))
        
        return max_area
