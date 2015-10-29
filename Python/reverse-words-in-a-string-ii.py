class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        def reverse_substr(s, start, end):
            end -= 1
            while start<end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        n = len(s)
        reverse_substr(s, 0, n)
        
        start = 0
        
        for i in xrange(n):
            if s[i] == ' ':
                reverse_substr(s, start, i)
                start = i+1
        
        reverse_substr(s, start, n)