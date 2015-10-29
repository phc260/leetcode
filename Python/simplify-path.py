class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        dirs = [i for i in path.split('/') if i!='.' and i!='']
        stk = []
        
        for i in dirs:
            if i=='..':
                if stk:
                    stk.pop()
            else:
                stk.append(i)
        if stk:
            ans = ''
            for i in stk:
                ans += '/'+i
            return ans
        else:
            return '/'