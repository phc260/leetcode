# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def traverse(self, p, sum):
        if p.left:
            agree = self.traverse(p.left,sum-p.val)
            if agree:
                return True
                
        if p.right:
            agree = self.traverse(p.right,sum-p.val)
            if agree:
                return True
                
        if p.left==p.right==None:
            return p.val==sum
            
        return False
        
    def hasPathSum(self, root, sum):
        return self.traverse(root, sum) if root else False