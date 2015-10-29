class WordDictionary:
    class TrieNode:
    # Initialize your data structure here.
        def __init__(self):
            self.child = {}
            # eow = end of word
            self.eow = False
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def __init__(self):
        self.root = self.TrieNode()
        
    def addWord(self, word):
        n = self.root
        for c in word:
            if c not in n.child:
                n.child[c] = self.TrieNode()
            n = n.child[c]
        n.eow = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        def search(idx, n):
            if idx>=len(word): return n.eow
            if not n.child: return False
            if word[idx]=='.':
                for c in n.child:
                    if search(idx+1, n.child[c]):
                        return True
                else:
                    return False
            elif word[idx] not in n.child:
                return False
            else:
                return search(idx+1, n.child[word[idx]])
                
        return search(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")