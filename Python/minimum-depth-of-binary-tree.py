# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
INT_MAX = 2147483647
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root: return 0
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        
        if l==r==0: return 1
        
        if l==0: l = INT_MAX
        if r==0: r = INT_MAX
        
        return 1+min(l, r)
