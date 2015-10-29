# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        def isSymmetric(n1, n2):
            if not n1: return n2==None
            if not n2: return False
            if n1.val!=n2.val: return False
            if not isSymmetric(n1.left, n2.right): return False
            if not isSymmetric(n1.right, n2.left): return False
            return True
        return isSymmetric(root, root)
