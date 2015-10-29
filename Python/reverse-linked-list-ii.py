# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        
        dummy.next = head
        
        pre = dummy
        cur = head
        
        for i in range(1,m):
            pre = cur
            cur = cur.next
            
        p1 = p2 = None
        
        if cur:
            p1 = cur.next
        if p1:
            p2 = p1.next
            
        for i in range(m,n):
            p1.next = cur
            cur = p1
            p1 = p2
            if p2:
                p2 = p2.next
                
        pre.next.next = p1
        pre.next = cur
                
        return dummy.next
        
