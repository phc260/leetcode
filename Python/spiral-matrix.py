class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix: return []
        r = len(matrix)
        c = len(matrix[0])
        left, right, top, down = 0, c-1, 0, r-1
        ans = []
        
        while left<right and top<down:
            for i in xrange(right-left): ans.append(matrix[top][left+i])
            for i in xrange(down-top): ans.append(matrix[top+i][right])
            for i in xrange(right-left): ans.append(matrix[down][right-i])
            for i in xrange(down-top): ans.append(matrix[down-i][top])
            left += 1; right -= 1; top += 1; down -= 1

        if top==down:
            for i in xrange(right-left+1): ans.append(matrix[top][left+i])
        elif right==left:
            for i in xrange(down-top+1): ans.append(matrix[top+i][left])
        
        return ans
