from collections import Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for val, count in counter.items():
            heappush(heap, (count, val))
            if len(heap) > k:
                heappop(heap)
        return [val for count, val in heap]