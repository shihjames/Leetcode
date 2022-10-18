"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(cur_node):
            if cur_node in cloned:
                return cloned[cur_node]
            copy = Node(cur_node.val)
            cloned[cur_node] = copy
            
            for neighbor in cur_node.neighbors:
                copy.neighbors.append(dfs(neighbor)) 
            return copy
        
        if not node:
            return None
        cloned = {}
        return dfs(node)