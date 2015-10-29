class Solution:
    class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.child = {}
            # eow = end of word
            self.eow = False
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        r = len(board)
        c = len(board[0])
        visited = [[False]*c for i in xrange(r)]
        
        root = self.TrieNode()
        ans = []
        s = set([])
        
        def addWord(word):
            n = root
            for c in word:
                if c not in n.child:
                    n.child[c] = self.TrieNode()
                n = n.child[c]
            n.eow = True
        
        def search(node, partial, i, j):
            if node.eow:
                if partial not in s:
                    ans.append(partial)
                    s.add(partial)
            if 0<=i<r and 0<=j<c and not visited[i][j] and board[i][j] in node.child:
                visited[i][j] = True
                search(node.child[board[i][j]], partial+board[i][j], i-1, j)
                search(node.child[board[i][j]], partial+board[i][j], i+1, j)
                search(node.child[board[i][j]], partial+board[i][j], i, j-1)
                search(node.child[board[i][j]], partial+board[i][j], i, j+1)
                visited[i][j] = False
        
        # build Trie
        for word in words:
            addWord(word)
        
        for i in xrange(r):
            for j in xrange(c):
                search(root, '', i, j)
        return ans
