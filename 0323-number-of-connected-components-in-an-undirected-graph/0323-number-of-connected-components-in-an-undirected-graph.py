class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            for neighbor in neighbors[node]:
                dfs(neighbor)
                
        visited = set()
        neighbors = defaultdict(list)
        count = 0
        
        for start, end in edges:
            neighbors[start].append(end)
            neighbors[end].append(start)
            
        for node in neighbors:
            if node not in visited:
                count += 1
                dfs(node)
        
        return count + n - len(visited)
            
        