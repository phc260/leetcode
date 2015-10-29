# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
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
            
    def sortedListToBST(self, head):
        nums = []
        while head:
                nums.append(head.val);
                head = head.next
        return self.sortedArrayToBST(nums)
