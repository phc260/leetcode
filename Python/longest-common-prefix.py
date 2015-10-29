class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        
        m = len(strs)
        if m==0: return ''
        if m==1: return strs[0]
        
        n = min([len(i) for i in strs])
        
        prefix = ''
        
        for j in xrange(n):
            
            for i in xrange(1, m):
                if strs[i][j] != strs[0][j]:
                    return prefix
            else:  
                prefix += strs[0][j]
            
        return prefix