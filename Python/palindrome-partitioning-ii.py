class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        n = len(s)
        cut = [i-1 for i in xrange(n+1)]
        
        for i in xrange(n):
            
            #odd
            j = 0
            while i+j<n and i>=j and s[i+j]==s[i-j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j]+1)
                j += 1
                
            #even
            j = 0
            while i+j-1<n and i>=j-1 and s[i+j-1]==s[i-j]:
                cut[i+j] = min(cut[i+j], cut[i-j]+1)
                j += 1
        
        return cut[n]