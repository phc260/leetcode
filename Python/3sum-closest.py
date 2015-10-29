INT_MAX = 2147483647
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        
        min_diff = 65535
        
        ans = 0
        n = len(num)
        for i in xrange(n):
            start = i+1
            end = n-1
            
            while start<end:
                
                sum3 = num[i]+num[start]+num[end]
                
                if sum3 == target:
                    return sum3
                elif sum3<target:
                    start += 1
                else:
                    end -= 1
                    
                diff = abs(sum3 - target)
                
                if diff < min_diff:
                    min_diff = diff
                    ans = sum3
                    
        return ans