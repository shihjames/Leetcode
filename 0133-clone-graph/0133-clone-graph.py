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
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        cloned = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned[cur_node].neighbors.append(cloned[neighbor])
        return cloned[node] 
                
        
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         def dfs(cur_node):
#             if cur_node in cloned:
#                 return cloned[cur_node]
#             copy = Node(cur_node.val)
#             cloned[cur_node] = copy
            
#             for neighbor in cur_node.neighbors:
#                 copy.neighbors.append(dfs(neighbor)) 
#             return copy
        
#         if not node:
#             return None
#         cloned = {}
#         return dfs(node)