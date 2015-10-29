class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        hash = {}
        ans = set([])
        n = len(num)
        
        for i in xrange(n-1):
            for j in xrange(i+1,n):
                val = num[i] + num[j]
                if val in hash:
                    hash[val].append((i,j))
                else:
                    hash[val] = [(i, j)]
                
        for i in xrange(n):
            for j in xrange(i+1, n-2):
                T = target-num[i]-num[j]
                if T in hash:
                    for p,q in hash[T]:
                        if p>j:
                            ans.add((num[i],num[j],num[p],num[q]))
        
        return [list(i) for i in ans]