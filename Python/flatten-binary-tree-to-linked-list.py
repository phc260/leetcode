# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        
        if root:
            fl = self.flatten(root.left)
            fr = self.flatten(root.right)
            root.left = None
            root.right = fl
            tail = root
            while tail.right:
                tail = tail.right
                
            tail.right = fr
                
        return root
