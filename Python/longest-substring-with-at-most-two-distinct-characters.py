class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s, k=2):

        n = len(s)
        count = [0]*256
        j = 0
        distinct = 0
        max_len = 0
        
        for i in xrange(n):
            
            if count[ord(s[i])]==0: distinct += 1
            count[ord(s[i])] += 1
            
            while distinct>k:
                count[ord(s[j])] -= 1
                if count[ord(s[j])]==0: distinct -= 1
                j += 1
            
            max_len = max(max_len, i-j+1)
        
        return max_len
