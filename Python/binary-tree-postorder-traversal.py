# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        st = []
        ans = []
        
        if root:
            st.append(root)
            
            while st:
                
                cur = st.pop()
                ans.append(cur.val)
                
                if cur.left: st.append(cur.left)
                if cur.right: st.append(cur.right)
                
            ans.reverse()

        return ans