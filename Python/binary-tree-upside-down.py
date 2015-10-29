# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def upsideDownBinaryTree(self, root, parent=None):
        if not root: return parent
        new_root = self.upsideDownBinaryTree(root.left, root)
        root.left = parent.right if parent else None
        root.right = parent
        return new_root
