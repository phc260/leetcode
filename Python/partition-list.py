# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        sh = ListNode(x-1)
        gh = ListNode(x-1)
        
        st = sh
        gt = gh
        
        p = head
        
        while p:
            
            if p.val<x:
                st.next = p
                st = st.next
            else:
                gt.next = p
                gt = gt.next
                
            p = p.next

        st.next = gh.next
        gt.next = None
        
        return sh.next
