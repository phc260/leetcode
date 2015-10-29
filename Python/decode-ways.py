class Solution:
    # @param s, a string
    # @return an integer

        
    def numDecodings(self, s):
        def valid1(one):
            return 1 if one!='0' else 0
        
        def valid2(one, two):
            return 1 if one=='1' or (one=='2' and two<'7') else 0
            
        n = len(s)
        if n==0:
            return 0
        if n==1:
            return valid1(s)
        if not valid1(s[0]):
            return 0
        
        fi = 0
        fi_1 = valid1(s[0])*valid1(s[1]) + valid2(s[0], s[1])
        fi_2 = 1
        for i in xrange(2, n):
            if valid1(s[i]):
                fi += fi_1
            if valid2(s[i-1], s[i]):
                fi += fi_2
            if fi==0:
                return 0
            fi_2  = fi_1
            fi_1 = fi
            fi = 0
        return fi_1
