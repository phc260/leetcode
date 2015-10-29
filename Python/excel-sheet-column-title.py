class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        s = ''

        s += chr((n-1)%26 +65)
        n = (n-1)/26
            
        while n>0:
            s += chr((n-1)%26 +65)
            n = (n-1)/26
        
        return s[::-1]
