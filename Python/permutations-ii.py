class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        n = len(num)
        
        if n==0:
            return
        if n==1:
            return [num]
            
        num.sort()
        ans = []
        pre = None
        for i in xrange(n):
            if pre==num[i]: continue
        
            pre = num[i]
            for j in self.permuteUnique(num[0:i] + num[i+1:n]):
                ans.append([num[i]]+j)
        return ans