class Solution:
    # @return a boolean
    def isValid(self, s):
        st = []
        d = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in d:
                if st and d[i]==st[-1]: st.pop()
                else: return False
            else: st.append(i)
        return not st
