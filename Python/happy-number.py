class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        
        def sq_sum_of_digits(n):
            sq_sum = 0
            while n:
                i = n%10
                sq_sum += i*i
                n = n/10
            return sq_sum
            
        exist = set([])
        
        while n not in exist:
            exist.add(n)
            
            n = sq_sum_of_digits(n)
        
        return True if 1 in exist else False