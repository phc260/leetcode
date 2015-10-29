# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stk= []
        self.go_left(root)
        
    def go_left(self, node):
        while node:
            self.stk.append(node)
            node = node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stk

    # @return an integer, the next smallest number
    def next(self):
        top = self.stk.pop()
        self.go_left(top.right)
        return top.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
