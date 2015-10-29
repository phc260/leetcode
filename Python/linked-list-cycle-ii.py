# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slow = fast = head
        
        while fast:
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
            
            if slow==fast:
                break
        
        if not fast: return None
        
        slow = head
        
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        
        return fast
