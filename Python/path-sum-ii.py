# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def traverse(self, ans, st, p, sum):
        if not p:
            return
        
        st.append(p.val)
        if p.left:
            self.traverse(ans, st, p.left, sum - p.val)
        if p.right:
            self.traverse(ans, st, p.right, sum - p.val)
            
        if p.val==sum and not p.left and not p.right:
            ans.append(st[:])
        st.pop()
        
            
            
    def pathSum(self, root, sum):
        ans = []
        st = []
        
        if root:
            self.traverse(ans, st, root, sum)
        
        return ans