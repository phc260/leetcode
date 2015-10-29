INT_MAX = 2147483647
class Solution:
    # @param {string} S
    # @param {string} T
    # @return {string}
    def minWindow(self, S, T):
        counter = {}
        count = len(T)
        
        for char in T:
            if char not in counter: counter[char]=1
            else: counter[char] += 1
            
        j = 0
        min_win = INT_MAX
        start = 0
        
        for i in range(len(S)):
            if S[i] in counter:
                if counter[S[i]]>0: count-=1
                counter[S[i]]-=1
                
            if count==0:
                while j<i:
                    if S[j] in counter:
                        if counter[S[j]]<0:
                            counter[S[j]]+=1
                        else:
                            break
                    j += 1
                if min_win > i-j+1:
                    min_win = i-j+1
                    start = j
        return S[start:start+min_win] if min_win<INT_MAX else ''
