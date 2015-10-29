# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        def get_len(l):
            n = 0
            while l:
                n += 1
                l = l.next
            return n
            
        a = get_len(headA)
        b = get_len(headB)
        
        while a>b:
            headA = headA.next
            a -= 1
            
        while b>a:
            headB = headB.next
            b -= 1
            
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA
