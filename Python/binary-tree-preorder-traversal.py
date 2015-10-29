# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        stk = []
        ans = []
        if root: stk.append(root)
        while stk:
            root = stk.pop()
            ans.append(root.val)
            if root.right: stk.append(root.right)
            if root.left: stk.append(root.left)
        return ans
