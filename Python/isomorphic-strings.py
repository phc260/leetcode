class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        hash_s = {}
        hash_t = {}
        
        for i in xrange(len(s)):
            if s[i] in hash_s:
                if hash_s[s[i]]!=t[i]: return False
            else: hash_s[s[i]] = t[i]
                
            if t[i] in hash_t:
                if hash_t[t[i]]!=s[i]: return False
            else: hash_t[t[i]] = s[i]
                
        return True
