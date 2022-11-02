"""
Time = O(nlog(k))
Space = O(k)
"""
from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dis = (x ** 2) + (y ** 2)
            heappush(heap, (-dis, x, y))
            if len(heap) > k:
                heappop(heap)
        
        return [[x, y] for dis, x, y in heap] 