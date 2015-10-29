# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root==None: return 0
        if self.left_depth(root)==self.right_depth(root): return (1<<self.left_depth(root))-1;
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

    def left_depth(self, root):
        return 1+self.left_depth(root.left) if root else 0
    def right_depth(self, root):
        return 1+self.right_depth(root.right) if root else 0
