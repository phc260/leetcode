# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        carry=0; head=ListNode(0); cur=head
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            cur.next = ListNode((v1+v2+carry)%10)
            carry = (v1+v2+carry)/10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        if carry>0:
            cur.next = ListNode(1)
        return head.next