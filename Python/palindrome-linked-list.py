# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        p1 = p2 = head
        while p2:
            p1 = p1.next
            p2 = p2.next
            if p2: p2 = p2.next
        p1 = self.reverseList(p1)
        p2 = head
        while p1 and p2:
            if p1.val!=p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
        
    def reverseList(self, head):
        fake = ListNode(0)
        cur = head
        while cur:
            next = cur.next
            cur.next = fake.next
            fake.next = cur
            cur = next
        return fake.next

