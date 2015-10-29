class Solution:
    # @param {string} s
    # @return {string}
    # KMP algorithm
    def shortestPalindrome(self, s):
        A = s + s[::-1]
        count = len(A)*[0]
        for i in xrange(1, len(A)):
            idx = count[i-1]
            while idx>0 and A[i]!=A[idx]: idx = count[idx-1]
            if A[idx]==A[i]: idx += 1
            count[i] = idx
        return s[count[-1]:][::-1]+s if len(A) else ''
