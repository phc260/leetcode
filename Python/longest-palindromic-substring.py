class Solution:
    # @return a string
    def longestPalindrome(self, s):
        
        def is_palindrome_centre(s, p, q):
            n = len(s)
            while p>=0 and q<n:
                if s[p]!=s[q]: break
                p -= 1
                q += 1
            return (p+1, q-1)
        
        n = len(s)
        max_len = 0
        start = end = 0
        for i in xrange(n):

            p, q = is_palindrome_centre(s, i, i)
            if q-p+1>max_len:
                start = p
                end = q+1
                max_len = q-p+1
                
            p, q = is_palindrome_centre(s, i-1, i)
            if q-p+1>max_len:
                start = p
                end = q+1
                max_len = q-p+1
        
        return s[start:end]