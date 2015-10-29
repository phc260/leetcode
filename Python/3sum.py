class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        n = len(num)
        ans = []
        num.sort()
        
        for i in xrange(n-2):
            if i==0 or num[i]>num[i-1]:
                negate = -num[i]
                start = i+1
                end = n-1
                
                while start<end:
                    if num[start]+num[end] == negate:
                        ans.append([num[i], num[start], num[end]])
                        start += 1
                        end -= 1
                        
                        #remove dup sol
                        while (start < end and num[end]==num[end+1]): end -= 1
                        while (start < end and num[start] == num[start-1]): start += 1
                    elif num[start]+num[end] < negate:
						start += 1
                    else:
                        end -= 1
                    
        return ans
