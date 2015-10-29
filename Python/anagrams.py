class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        ans = []
        hashmap = {}
        
        for i in xrange(len(strs)):
            
            sorted_str = ''.join(sorted(strs[i]))
            
            if sorted_str in hashmap:
                hashmap[sorted_str].append(strs[i])
                
            else:
                hashmap[sorted_str] = [strs[i]]
                
        for sorted_str in hashmap:
            if len(hashmap[sorted_str])>1:
                for i in hashmap[sorted_str]:
                    ans.append(i)
                    
        return ans
