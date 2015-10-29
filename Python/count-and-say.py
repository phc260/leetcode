class Solution:
    # @return a string
    def countAndSay(self, n):
        
        ans = "1"
        
        for i in range(n-1):
            counter = 1
            tmp = ""
            for j in range(1, len(ans)):
                if ans[j] == ans[j-1]:
                    counter += 1
                else:
                    tmp += str(counter) + ans[j-1]
                    counter = 1
                    
            tmp += str(counter) + ans[len(ans)-1]
            
            ans  = tmp
            
        return ans
