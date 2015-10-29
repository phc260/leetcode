# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    
    def traverse(self, ans, root, lv):
        
        if root:
            if lv >= len(ans):
                ans.append([])
                
            ans[lv].append(root.val)
                
            self.traverse(ans, root.left, lv+1)
            self.traverse(ans, root.right, lv+1)
            
        
    def levelOrderBottom(self, root):
        ans = []
        self.traverse(ans, root, 0)
        ans.reverse()
        return ans