class Trie:
    class TrieNode:
    # Initialize your data structure here.
        def __init__(self):
            self.child = {}
            self.eow = False
    def __init__(self):
        self.root = self.TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        n = self.root
        for c in word:
            if c not in n.child:
                n.child[c] = self.TrieNode()
            n = n.child[c]
        n.eow = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        n = self.root
        for c in word:
            if c not in n.child:
                return False
            else:
                n = n.child[c]
        return n.eow

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        n = self.root
        for c in prefix:
            if c not in n.child:
                return False
            else:
                n = n.child[c]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")