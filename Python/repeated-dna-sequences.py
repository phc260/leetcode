class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        hash_map={};
        for i in xrange(len(s)-9):
            key=s[i:i+10];
            if(key not in hash_map):
                hash_map[key] = 1;
            else:
                hash_map[key] += 1;
        return [i for i in hash_map.keys() if hash_map[i]>1]
