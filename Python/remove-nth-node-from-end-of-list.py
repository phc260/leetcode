# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        ptr = []
        cur = head
        while cur:
            ptr.append(cur)
            cur = cur.next
        
        l = len(ptr)
        idx = l - n
        
        if idx==0:
            return head.next
        elif n==1:
            if l==1:
                return None
            else:
                ptr[l-2].next = None
        else:
            ptr[idx-1].next = ptr[idx+1]

        return head
