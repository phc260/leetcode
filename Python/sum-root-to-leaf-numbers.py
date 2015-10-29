# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def traverse(self, p, val):
        num = 0
        if p.left:
            num += self.traverse(p.left, val*10 + p.left.val)
        if p.right:
            num += self.traverse(p.right, val*10 + p.right.val)
            
        if not p.left and not p.right:
            return val
        else:
            return num
        
    def sumNumbers(self, root):
        return self.traverse(root, root.val) if root else 0