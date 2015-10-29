# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        
        if head:
            cur = head
            array = []
            
            while cur:
                array.append(cur)
                cur = cur.next
                
            n = len(array)
            
            for i in range((n-1)/2):
                array[i].next = array[n-1-i]
                array[n-1-i].next = array[i+1]

            array[n/2].next = None
        
        return head
