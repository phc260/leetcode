class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        tokens = s.split(' ')
        ans = ''
        for i in reversed(tokens):
            if i!='':
                ans += (i+' ')
        return ans.strip()
