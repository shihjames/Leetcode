"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
Time = O(V+E)
Space = O(V)
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            if node in cloned:
                return cloned[node]
            
            copy = Node(node.val)
            cloned[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        if not node:
            return None
        cloned = {}
        return dfs(node)