class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if s1==s2: return True
        if len(s1)!=len(s2): return False
        
        counter = [0]*26
        n = len(s1)
        
        for i in xrange(n):
            counter[ord(s1[i])-ord('a')] += 1
            counter[ord(s2[i])-ord('a')] -= 1
        
        for e in counter:
            if e!=0: return False
        
        for i in xrange(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True;
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True;
        
        return False
