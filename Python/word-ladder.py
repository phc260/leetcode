class Solution:
    # @param startWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, startWord, endWord, wordDict):
        def is_transformable(s, t):
            d = 0
            for i in xrange(len(s)):
                if s[i]!=t[i]: d+=1
                if d>1: return False
            return d==1
        
        start_table = set([startWord])
        end_table = set([endWord])
        start_dict = wordDict.copy()
        end_dict = wordDict.copy()
        start_count = 1
        end_count = 1
        
        while start_table and end_table:
            count = 0
            if len(start_table)*len(start_dict) <= len(end_table)*len(end_dict):
                tmp_table = start_table.copy()
                for word in tmp_table:
                    start_table.remove(word)
                    if is_transformable(word, endWord):
                        return start_count+1
                    for i in xrange(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            next_word = word[:i]+c+word[i+1:]
                            if next_word in start_dict:
                                start_table.add(next_word)
                                start_dict.remove(next_word)
                                count = 1
                start_count += count
            else:
                tmp_table = end_table.copy()
                for word in tmp_table:
                    end_table.remove(word)
                    if is_transformable(word, startWord):
                        return end_count+1
                    for i in xrange(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            next_word = word[:i]+c+word[i+1:]
                            if next_word in end_dict:
                                end_table.add(next_word)
                                end_dict.remove(next_word)
                                count = 1
                end_count += count
            if start_table & end_table: return start_count+end_count-1
        return 0
