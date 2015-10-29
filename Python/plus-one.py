class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        n = len(digits)
        carry = 0
        digits[n-1] += 1
        for i in range(n-1, -1, -1):
            digits[i] += carry
            if digits[i]>9:
                carry = 1
                digits[i] -= 10
            else:
                carry = 0
            
        if carry>0:
            digits.insert(0, 1)
            
        return digits