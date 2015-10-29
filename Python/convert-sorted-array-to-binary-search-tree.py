# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        def BST(b, e):
            node = None
            if b<e:
                i = (b+e)/2
                node = TreeNode(nums[i])
                node.left = BST(b, i)
                node.right = BST(i+1, e)
            return node
            
        return BST(0, len(nums))
