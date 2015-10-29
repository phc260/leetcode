# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return None
        
        cur = head
        
        # insert a copy after each node
        while cur:
            new_node = RandomListNode(cur.label)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        
        cur = head
        
        # copy random pointers
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        new_head = new_cur = head.next
        
        while new_cur.next:
            cur.next = new_cur.next
            cur = cur.next
            new_cur.next = cur.next
            new_cur = new_cur.next
            
        new_cur.next = cur.next = None
        
            
        return new_head