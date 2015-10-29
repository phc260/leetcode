class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        max_len = 0
        
        s = set(num)
        
        while s:
            target = s.pop()
            length = 1
            
            lower = target-1
            
            while lower in s:
                s.remove(lower)
                lower -= 1
                length += 1
            lower += 1
            
            higher = target+1
            
            while higher in s:
                s.remove(higher)
                higher += 1
                length += 1
                    
            max_len = max(max_len, length)
            
        return max_len
