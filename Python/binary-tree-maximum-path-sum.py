# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
INT_MIN = -2147483648
class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        import sys
        self.max_path_sum = -sys.maxsize-1
        
    def maxPathSum(self, root):
        self.get_max(root)
        return self.max_path_sum
        
    def get_max(self, root):
        if not root:
            return 0
        left = self.get_max(root.left)
        right = self.get_max(root.right)
        
        sum_all = root.val
        
        if left>0:
            sum_all += left
        if right>0:
            sum_all += right
            
        self.max_path_sum = max(self.max_path_sum, sum_all)
        
        return max(0, left, right)+root.val
