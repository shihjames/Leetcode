class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.size = 1
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            if node.parent is not node:
                node.parent = find(node.parent)

            return node.parent
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            
            # Found nodes with same parents
            if p1 is p2:
                return False
            
            # p1 be the parent
            if p1.size > p2.size:
                p2.parent = p1
                p1.size += p2.size
            # p2 be the parent
            else:
                p1.parent = p2
                p2.size += p1.size
                
            return True
        
        nodes = {}
        for i in range(1, len(edges) + 1):
            nodes[i] = Node(i)
        
        for n1, n2 in edges:
            if not union(nodes[n1], nodes[n2]):
                return [n1, n2]
            
        