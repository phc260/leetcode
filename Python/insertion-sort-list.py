# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head: return head
        
        fake = ListNode(0)
        fake.next = head
        cur = head
        
        while cur.next:
            
            if cur.next.val<cur.val:
                pre = fake
                while pre.next.val<cur.next.val:
                    pre = pre.next
                next = cur.next
                cur.next = next.next
                next.next = pre.next
                pre.next = next
            else:
                cur = cur.next

        return fake.next
