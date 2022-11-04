"""
Time = O(V+E)
Space = O(V+E)
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in neighbors[node]:
                if neighbor != prev:
                    if not dfs(neighbor, node):
                        return False
            return True
            
        visited = set()
        neighbors = defaultdict(list)
        for start, end in edges:
            neighbors[start].append(end)
            neighbors[end].append(start)
        
        return dfs(0, -1) and len(visited) == n
        
        