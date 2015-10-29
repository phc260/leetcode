class Solution:
    # @param an integer
    # @return a list of string
        
    def generateParenthesis(self, n):
        
        def generate(ans, sample, l, r):
            if l==r==0:
                ans.append(sample[:])
            if l>0:
                generate(ans, sample[:]+'(', l-1, r)
            if r>0 and l<r:
                generate(ans, sample[:]+')', l, r-1)
        ##############################################
        ans = []
        sample = '('
        
        if n>0:
            generate(ans, sample[:], n-1, n)
            
        return ans
