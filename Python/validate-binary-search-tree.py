# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
INT_MAX = 2147483647
INT_MIN = -2147483648
class Solution:
    # @param root, a tree node
    # @return a boolean
        
    def isValidBST(self, root):
	
        def verify(p, MIN, MAX):
            if not p: return True
			
            if p.val>MIN and p.val<MAX and verify(p.left, MIN, p.val) and verify(p.right, p.val, MAX):
                return True
            else:
                return False
        ##############################################################################################
				
        return verify(root, INT_MIN, INT_MAX)
