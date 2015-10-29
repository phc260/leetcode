class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        
        if numerator==0 or denominator==0:
            return '0'
        
        ans = ''
        
        if (numerator<0) ^ (denominator<0):
            ans += '-'
        
        numerator = abs(numerator)
        denominator = abs(denominator)
            
        ans += str(numerator/denominator)

        r = (numerator%denominator)*10
        
        if r==0:
            return ans
        
        # key = r, val = q
        hash_map = {}
        
        ans += '.'
        while r:
            
            if r in hash_map:
                return ans[0:hash_map[r]] + '(' + ans[hash_map[r]:] + ')'
            else:
                hash_map[r] = len(ans)
                ans += str(r/denominator)
                r = (r%denominator)*10
        
        return ans