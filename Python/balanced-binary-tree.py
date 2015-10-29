# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        def is_balanced(root):
            if not root: return -1
            lheight = is_balanced(root.left)
            if lheight==-2: return -2
            rheight = is_balanced(root.right)
            if rheight==-2: return -2
            return -2 if abs(lheight-rheight)>1 else 1+max(lheight, rheight)
        return is_balanced(root)!=-2
