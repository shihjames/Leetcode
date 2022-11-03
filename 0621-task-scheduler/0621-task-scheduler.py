from collections import Counter
from heapq import heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        counter = Counter(tasks)
        heap = []
        queue = deque()
        cur_time = 0
        for task, count in counter.items():
            heappush(heap, -count)
        
        while heap or queue:
            cur_time += 1
            if heap:
                count = heappop(heap) + 1
                if count != 0:
                    queue.append((count, cur_time + n))
            if queue and queue[0][1] == cur_time:
                task_count, time = queue.popleft()
                heappush(heap, task_count)
        
        return cur_time
        
        