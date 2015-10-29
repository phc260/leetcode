# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        cur = head = ListNode(0)
        
        while l1 and l2:
            if l1.val<l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
        
        return head.next
            
        
    def sortList(self, head):
        if head==None or head.next==None:
            return head
        
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head1 = head
        head2 = slow.next
        slow.next = None
        
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        
        return self.merge(head1, head2)