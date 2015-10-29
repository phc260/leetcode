class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        ans = []
        if numRows<=0:
            return ans

        a = b = 0
        ans.append([1])
        for i in xrange(numRows-1):
            
            row = ans[i][:]
            a = 1
            
            for j in xrange(1, len(row)):
                b = row[j]
                row[j] = a+b
                a = b
            
            row.append(1)
            
            ans.append(row)
        return ans
