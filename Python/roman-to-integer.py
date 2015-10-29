class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        ans = 0
        pre_c2n = 100000
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for c in s:
            cur_c2n = dic[c]
            ans += cur_c2n
            
            if pre_c2n < cur_c2n:
                ans -= pre_c2n<<1
            
            pre_c2n = cur_c2n
            
        return ans
