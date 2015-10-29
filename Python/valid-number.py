class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        i = 0
        n = len(s)
        
        while i<n and s[i]==' ':  i+=1
        if i<n and (s[i]=='-' or s[i]=='+'):  i+=1
        
        
        is_numberic = False
        
        
        while i<n and s[i].isdigit():
            i+=1
            is_numberic = True
        
        if i<n and s[i]=='.':
            i+=1
            
            while i<n and s[i].isdigit():
                i+=1
                is_numberic = True
        
        
        if is_numberic and i<n and s[i]=='e':
            i+=1
            is_numberic = False
            
            if i<n and (s[i]=='-' or s[i]=='+'):  i+=1
            
            while i<n and s[i].isdigit():
                i+=1
                is_numberic = True
        
        
        while i<n and s[i]==' ':  i+=1
        
        
        return is_numberic and i==n
