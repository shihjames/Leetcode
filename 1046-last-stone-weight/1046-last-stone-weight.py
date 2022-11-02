from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heappush(heap, -stone)
        
        while len(heap) > 1:
            s1 = -heappop(heap)
            s2 = -heappop(heap)
            print(s1, s2)
            if s1 > s2:
                heappush(heap, -(s1 - s2))
        
        return -heap[0] if heap else 0