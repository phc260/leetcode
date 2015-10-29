class Solution:
    # @return a list of strings, [s1, s2]
    d = ['','', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def letterCombinations(self, digits):
      
        pre = ['']
       
        for k in digits:
            now = [i for i in self.d[int(k)]]
            pre = [i+j for i in pre for j in now]

        return pre