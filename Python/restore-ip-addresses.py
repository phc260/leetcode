class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        
        ans = []
        
        def partition(idx, part, resultIP):
            if part>=5:
                if idx>=len(s):
                    ans.append(resultIP[:len(resultIP)-1])
                return
    
            if idx>=len(s): return
    
            partition(idx+1, part+1, resultIP+s[idx]+'.')
    
            if s[idx]=='0': return
    
            for i in xrange(idx+1, min(len(s), idx+3)):
                v = int(s[idx:i+1])
                if v<256:
                    partition(i+1, part+1, resultIP+s[idx:i+1]+'.')


        partition(0, 1, '')
        return ans
