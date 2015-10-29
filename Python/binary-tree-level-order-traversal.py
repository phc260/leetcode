# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        def traverse(root, lv):
            if root:
                if lv >= len(ans): ans.append([])
                ans[lv].append(root.val)
                traverse(root.left, lv+1)
                traverse(root.right, lv+1)

        ans = []
        traverse(root, 0)
            
        return ans
