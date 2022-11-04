class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            # Found nodes with same parents
            if p1 == p2:
                return False
            # p1 be the parent
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
                
            return True

        parent = []
        rank = []
        for i in range(len(edges) + 1):
            parent.append(i)
            rank.append(1)
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
        