# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        
        prev = fake = ListNode(0)
        curr = head
        prev.next = curr
        
        while curr:
            if curr.val==val:
                curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
        
        return fake.next
