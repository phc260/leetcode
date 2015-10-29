class Solution:
    # @return a string
    def getPermutation(self, n, k):
        perm = 1
        ans = ''
        num = []
        
        for i in xrange(n):
            num.append(i+1)
            perm *= (i+1)
            
        k -= 1
            
        for i in xrange(n):
            perm /= (n-i)
            
            ans += str(num.pop(k/perm))
            
            k %= perm
            
        return ans