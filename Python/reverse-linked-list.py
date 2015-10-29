# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head, tail=None):
        prev = next = None
        while head!=tail:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
