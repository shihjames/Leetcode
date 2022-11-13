"""
Time = O(Elog(V))
Space = O(V+E)
"""
from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        
        for start, end, weight in times:
            edges[start].append((end, weight))
        
        heap = [(0, k)]
        visited = set()
        res = 0
        
        while heap:
            weight, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            
            res = max(res, weight)
            
            for neighbor, cur_weight in edges[node]:
                if neighbor not in visited:
                    heappush(heap, (cur_weight + weight, neighbor))
                    
        return res if len(visited) == n else -1
    