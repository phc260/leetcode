# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        def genBST(start, end):
            if start>end: return [None]

            roots = []
            for i in range(start, end+1):
                left = genBST(start, i-1)
                right = genBST(i+1, end)
                
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        roots.append(root)
            return roots
                        
        return genBST(1, n)
