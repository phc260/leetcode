# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
        
    def cloneGraph(self, node):
        
        if not node:
            return None
        
        stk = []
        visited = {}
        new_node = UndirectedGraphNode(node.label)
        stk.append(node)
        visited[node] = new_node
        
        
        while stk:
            this = stk.pop()
            for neighbor in this.neighbors:
                if neighbor not in visited:
                    copy = UndirectedGraphNode(neighbor.label)
                    visited[this].neighbors.append(copy)
                    visited[neighbor] = copy
                    stk.append(neighbor)
                else:
                    visited[this].neighbors.append(visited[neighbor])
        
        
        return new_node