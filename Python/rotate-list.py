# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):

        table = []
        
        cur = head
        while cur:
            table.append(cur)
            cur = cur.next

        n = len(table)
        if n<2: return head
        
        k %= n;
        
        if k>0:
            table[n-k-1].next = None
            table[n-1].next = table[0]
            return table[n-k]
        else:
            return head