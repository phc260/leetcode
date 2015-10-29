# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        head = cur = ListNode(0)
        
        i = 0
        while i<len(lists):
            if lists[i]==None:
                lists.pop(i)
            else:
                i += 1
            
        while len(lists):
            idx = 0
            for i in xrange(1,len(lists)):
                if lists[i].val<lists[idx].val:
                    idx = i
            cur.next = lists[idx]
            cur = cur.next
            lists[idx] = lists[idx].next
            
            if not lists[idx]:
                lists.pop(idx)
                
        return head.next