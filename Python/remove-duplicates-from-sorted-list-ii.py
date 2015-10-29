# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
INT_MIN = -2147483648
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        
        if not head:
            return None
        
        dummy = ListNode(INT_MIN)
        dummy.next = head
        
        p1 = dummy
        
        while p1.next:
            p2 = p1.next
            
            if not p2.next:
                break
                
            if p2.val==p2.next.val:
                p3 = p2.next
                
                while p3 and p3.val==p2.val:
                    p3 = p3.next
                    
                p1.next = p3
                
            else:
                p1 = p1.next
            
        return dummy.next