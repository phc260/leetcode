# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        
        n = len(preorder)
        
        if n == 0:
            return None
            
        v = preorder[0]
        root = TreeNode(v)
        idx = inorder.index(v)
        
        root.left = self.buildTree(preorder[1:idx+1], inorder[0:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        
        return root
