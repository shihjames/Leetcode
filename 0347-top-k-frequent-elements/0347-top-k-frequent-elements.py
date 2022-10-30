"""
Time = O(nlog(k))
Space = O(n+k)
"""
from heapq import heappush, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        counter = Counter(nums)
        
        for num, count in counter.items():
            freq[count].append(num)
            
        res = []
        
        for i in range(len(freq)-1, 0, -1):
            if freq[i]:
                res.extend(freq[i])
                if len(res) == k:
                    return res
        
        
#         counter = Counter(nums)
#         heap = []
        
#         for num, count in counter.items():
#             heappush(heap, (count, num))
#             if len(heap) > k:
#                 heappop(heap)
                
#         return [num for count, num in heap]