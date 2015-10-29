tion for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        stk = []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            k -= 1
            if k<=0:
                return root.val
            root = root.right

