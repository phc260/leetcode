INT_MAX = 2147483647
INT_MIN = -2147483648
class Solution:
    # @return an integer
    def myAtoi(self, str):
        
        i = 0
        val = 0
        n = len(str)
        signed = False
        while i<n and str[i]==' ':
            i += 1
        
        if i<n:
            if str[i]=='-':
                signed = True
                i += 1
            elif str[i]=='+':
                i += 1

        while i<n and str[i].isdigit():
            d = ord(str[i]) - ord('0')
            val = val*10
            
            if signed:
                if INT_MIN+val>=-d:
                    return INT_MIN
            else:
                if INT_MAX-val<=d:
                    return INT_MAX
            
            val += d
            i += 1
                    
        return -val if signed else val
