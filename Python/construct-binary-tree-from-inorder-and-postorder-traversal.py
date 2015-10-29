# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        
        n = len(postorder)
        
        if n == 0:
            return None
            
        v = postorder[n-1]
        root = TreeNode(v)
        idx = inorder.index(v)
        
        root.left = self.buildTree(inorder[0:idx], postorder[0:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:n-1])
        
        return root
