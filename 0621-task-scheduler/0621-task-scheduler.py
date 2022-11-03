"""
Time = O(n)
Space = O(1)
"""
from collections import Counter, deque
from heapq import heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        # O(26) = O(1)
        counter = Counter(tasks)
        heap = []
        queue = deque()
        cur_time = 0
        # O(26), Add task count in to max heap
        for task, count in counter.items():
            heappush(heap, -count)
         # Schedule tasks if heap and queue are not empty
        # O(n+m)
        while heap or queue:
            cur_time += 1
            if heap:
                # O(log(26))
                count = heappop(heap) + 1
                if count != 0:
                    queue.append((count, cur_time + n))
            if queue and queue[0][1] == cur_time:
                task_count, time = queue.popleft()
                # O(log(26))
                heappush(heap, task_count)
        
        return cur_time
        
        