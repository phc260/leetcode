class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if haystack=='' and needle=='':
            return 0
        return haystack.find(needle)