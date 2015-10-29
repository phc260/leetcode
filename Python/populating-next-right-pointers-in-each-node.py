# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or not root.left: return
        queue = [root]
        nextrow = []
        while len(queue)>0:
            e = queue.pop(0)
            if e.left is not None:
                nextrow.append(e.left)
                nextrow.append(e.right)
            if len(queue)>0:
                e.next = queue[0]
            else:
                queue = nextrow
                nextrow = []
