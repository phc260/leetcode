class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        
        n1 = len(v1)
        n2 = len(v2)
        n = min(n1, n2)
        
        for i in xrange(n):
            if v1[i]>v2[i]:
                return 1
            if v1[i]<v2[i]:
                return -1
                
        if n1>n2:
            for i in xrange(n, n1):
                if v1[i]>0:
                    return 1
        elif n1<n2:
            for i in xrange(n, n2):
                if v2[i]>0:
                    return -1
        
        return 0