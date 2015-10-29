class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num = 0
        for c in s:
            num = num*26 + ord(c) - ord('A') +1
        return num
