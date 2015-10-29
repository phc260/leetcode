class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        vec = [0]*(len(num1)+len(num2)+1)
        for i in xrange(len(num1)):
            d1 = int(num1[i])
            carry = 0
            for j in xrange(len(num2)):
                d2 = int(num2[j])
                
                t = d1*d2 + carry + vec[i+j]
                vec[i+j] = t%10
                carry = t/10
            if carry>0:
                vec[i+len(num2)] = carry
        
        while vec and vec[-1]==0:
            vec.pop()
        
        if not vec: return '0'
        
        ans = ''
        
        for i in xrange(len(vec)-1, -1, -1):
            ans += str(vec[i])
        return ans
