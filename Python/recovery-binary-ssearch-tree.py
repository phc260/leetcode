# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def __init__(self):
        self.pre = self.first = self.second = None
    def recoverTree(self, r):
        
        def find(root):
            if not root: return
            find(root.left)
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val>root.val:
                    if not self.first:
                        self.first = self.pre
                    self.second = root
                self.pre = root
            find(root.right)
            
        find(r)
        self.first.val, self.second.val = self.second.val, self.first.val
