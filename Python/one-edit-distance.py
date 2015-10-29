class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):
        m = len(s)
        n = len(t)
        
        if abs(m-n)>1:
            return False
            
        if m>n:
            return self.isOneEditDistance(t, s)
        
        i = 0
        shift = n-m
        
        while i<m and s[i]==t[i]:
            i += 1
            
        if i==m:
            return shift>0
        
        if shift==0:
            i += 1
            
        while i<m and s[i]==t[i+shift]:
            i += 1
            
        return i==m