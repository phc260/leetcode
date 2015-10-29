class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseList(self, start, end):
        fake = ListNode(0)
        cur = tail = start
        end_next = end.next
        
        while cur!=end_next:
            next = cur.next
            cur.next = fake.next
            fake.next = cur
            
            cur = next
        tail.next = end_next
        
        return (fake.next, tail)
    
    
    def reverseKGroup(self, head, k):
            
        pre = fake = ListNode(0)
        start = end = fake.next = head
        for i in xrange(k-1):
             if end: end = end.next
        while end:
            
            # reverse sub linkedlist
            
            start, end = self.reverseList(start, end)
            print start.val, end.val
            pre.next = start
            
            pre = end
            start = end.next
            
            for i in xrange(k):
                if end: end = end.next
            
        return fake.next
