"""
Time = O(M*N)
Space = O(N)
Where N = # of equations, M = # of Quries
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def traverse(start, end, cur, visited):
            if start not in graph and end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            ret = -1.0
            visited.add(start)
            neighbors = graph[start]
            
            if end in neighbors:
                ret = cur * neighbors[end]
            else:
                for neighbor, val in neighbors.items():
                    if neighbor not in visited:
                        ret = traverse(neighbor, end, cur*val, visited)
                        if ret != -1:
                            break
            
            visited.remove(start)
            return ret  
            
        graph = defaultdict(dict)
        
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = float(values[i])
            graph[equations[i][1]][equations[i][0]] =  1 / values[i]

        
        visited = set()
        res = []
        
        for query in queries:
            res.append(traverse(query[0], query[1], 1, visited))
        
        return res
        
        
            