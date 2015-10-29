class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        t = s.strip().rpartition(' ')
        return len(t[-1]) if t[-1] else len(t[0])
