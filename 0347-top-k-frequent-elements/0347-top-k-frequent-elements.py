"""
Time = O(nlog(k))
Space = O(n+k)
"""
from heapq import heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        
        for num, count in counter.items():
            heappush(heap, (count, num))
            if len(heap) > k:
                heappop(heap)
                
        return [num for count, num in heap]