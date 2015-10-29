class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        
        n = len(s)
        exist = [False]*256
        max_len = 0
        j = 0
        for i in xrange(n):
            while exist[ord(s[i])]:
                exist[ord(s[j])] = False
                j += 1
                
            exist[ord(s[i])] = True
            max_len = max(max_len, i-j+1)
            
        return max_len
