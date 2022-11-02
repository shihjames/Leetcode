from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # Iterate through the nums
        for num in nums:
            # First push the num to the heap
            heappush(heap, num)
            # Check the length of the heap is smaller than k
            if len(heap) > k:
                # Pop out the smallst one
                heappop(heap)
        
        # The smallest element in the heap will be the kth smallest element in the nums
        k_largest = heappop(heap)
        return k_largest