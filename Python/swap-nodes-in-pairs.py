# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        prev = fake = ListNode(0)
        fake.next = head
        while prev.next and prev.next.next:
            p1 = prev.next
            p2 = p1.next
            prev.next = p2
            p1.next = p2.next
            p2.next = p1
            prev = p1
        return fake.next
